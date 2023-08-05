r"""This module implements functions to sample values from continuous
univariate distribution supported on a bounded interval."""

from __future__ import annotations

__all__ = [
    "asinh_uniform",
    "log_uniform",
    "rand_asinh_uniform",
    "rand_log_uniform",
    "rand_trunc_cauchy",
    "rand_trunc_exponential",
    "rand_trunc_half_cauchy",
    "rand_trunc_half_normal",
    "rand_trunc_log_normal",
    "rand_trunc_normal",
    "rand_uniform",
    "trunc_cauchy",
    "trunc_exponential",
    "trunc_half_cauchy",
    "trunc_half_normal",
    "trunc_log_normal",
    "trunc_normal",
    "uniform",
]

import math

import torch
from torch import Tensor
from torch.distributions import (
    Cauchy,
    Exponential,
    HalfCauchy,
    HalfNormal,
    LogNormal,
    Normal,
)

from startorch.utils.tensor import shapes_are_equal


def rand_trunc_cauchy(
    size: list[int] | tuple[int, ...],
    loc: float = 0.0,
    scale: float = 1.0,
    min_value: float = -2.0,
    max_value: float = 2.0,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a truncated
    Cauchy distribution.

    Args:
    ----
        size (list or tuple): Specifies the tensor shape.
        loc (float, optional): Specifies the location of the Cauchy
            distribution. Default: ``0.0``
        scale (float, optional): Specifies the scale of the Cauchy
            distribution. Default: ``1.0``
        min_value (float, optional): Specifies the minimum value.
            Default: ``-2.0``
        max_value (float, optional): Specifies the maximum value.
            Default: ``2.0``
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from
            a truncated Cauchy distribution

    Raises:
    ------
        ValueError if the ``max_value`` and ``min_value`` parameters
            are not valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import rand_trunc_cauchy
        >>> rand_trunc_cauchy(
        ...     (2, 3), loc=1.0, scale=2.0, min_value=-3.0, max_value=3.0
        ... )  # doctest:+ELLIPSIS
        tensor([[...]])
    """
    if max_value < min_value:
        raise ValueError(
            f"`max_value` ({max_value}) has to be greater or equal to `min_value` ({min_value})"
        )
    distribution = Cauchy(loc=loc, scale=scale)
    # Values are generated by using a truncated uniform distribution and
    # then using the inverse CDF for the Cauchy distribution.
    # Get upper and lower CDF values
    lo, up = distribution.cdf(torch.tensor([min_value, max_value]))
    return distribution.icdf(rand_uniform(size, low=lo, high=up, generator=generator)).clamp(
        min=min_value, max=max_value
    )


def trunc_cauchy(
    loc: Tensor,
    scale: Tensor,
    min_value: Tensor,
    max_value: Tensor,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a truncated
    Cauchy distribution.

    Args:
    ----
        loc (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the location/median of
            the Cauchy distribution.
        scale (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the scale
            of the Cauchy distribution.
        min_value (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the minimum value.
        max_value (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the maximum value.
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from
            a truncated Cauchy distribution

    Raises:
    ------
        ValueError if the ``loc``, ``scale``, ``max_value`` and
            ``min_value`` parameters are not valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import trunc_cauchy
        >>> trunc_cauchy(
        ...     loc=torch.tensor([1.0, 0.0, -1.0]),
        ...     scale=torch.tensor([1.0, 3.0, 5.0]),
        ...     min_value=torch.tensor([-5.0, -10.0, -15.0]),
        ...     max_value=torch.tensor([5.0, 10.0, 15.0]),
        ... )  # doctest:+ELLIPSIS
        tensor([...])
    """
    if not shapes_are_equal((loc, scale, min_value, max_value)):
        raise ValueError(
            f"Incorrect shapes. The shapes of all the input tensors must be equal: loc={loc.shape}"
            f"  scale={scale.shape}  min_value={min_value.shape}  max_value={max_value.shape}"
        )
    if torch.any(scale <= 0.0):
        raise ValueError("All the `scale` values have to be greater than 0")
    if torch.any(max_value < min_value):
        raise ValueError(
            "Found at least one value in `min_value` that is higher than its associated "
            "`max_value`"
        )
    distribution = Cauchy(loc=loc, scale=scale)
    # Values are generated by using a truncated uniform distribution and
    # then using the inverse CDF for the Cauchy distribution.
    # Get upper and lower CDF values
    lo, up = distribution.cdf(torch.stack([min_value, max_value]))
    return distribution.icdf(uniform(low=lo, high=up, generator=generator)).clamp(
        min=min_value, max=max_value
    )


def rand_trunc_exponential(
    size: list[int] | tuple[int, ...],
    rate: float = 1.0,
    max_value: float = 5.0,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a truncated
    Exponential distribution.

    Args:
    ----
        size (list or tuple): Specifies the tensor shape.
        rate (float, optional): Specifies the rate of the Exponential
            distribution. Default: ``1.0``
        max_value (float, optional): Specifies the maximum value.
            Default: ``5.0``
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from a
            truncated Exponential distribution

    Raises:
    ------
        ValueError if the ``max_value`` parameter is not valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import rand_trunc_exponential
        >>> rand_trunc_exponential((2, 3), rate=1.0, max_value=3.0)  # doctest:+ELLIPSIS
        tensor([[...]])
    """
    if max_value <= 0:
        raise ValueError(f"`max_value` has to be greater than 0 (received: {max_value})")
    distribution = Exponential(rate=rate)
    # Values are generated by using a truncated uniform distribution and
    # then using the inverse CDF for the Exponential distribution.
    # Get upper and lower CDF values
    up = distribution.cdf(torch.tensor(max_value)).item()
    return distribution.icdf(rand_uniform(size, low=0.0, high=up, generator=generator)).clamp(
        max=max_value
    )


def trunc_exponential(
    rate: Tensor,
    max_value: Tensor,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a truncated
    Exponential distribution.

    Args:
    ----
        rate (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the rate
            of the Exponential distribution.
        max_value (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the maximum value.
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from
            a truncated Exponential distribution.

    Raises:
    ------
        ValueError if the ``rate`` and ``max_value`` parameter are not
            valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import trunc_exponential
        >>> trunc_exponential(
        ...     rate=torch.tensor([1.0, 3.0, 5.0]),
        ...     max_value=torch.tensor([5.0, 10.0, 15.0]),
        ... )  # doctest:+ELLIPSIS
        tensor([...])
    """
    if rate.shape != max_value.shape:
        raise ValueError(
            "Incorrect shapes. The shapes of all the input tensors must be equal:  "
            f"rate={rate.shape}  max_value={max_value.shape})"
        )
    if torch.any(rate <= 0.0):
        raise ValueError("All the `rate` values have to be greater than 0")
    if torch.any(max_value <= 0.0):
        raise ValueError("Found at least one value in `max_value` that is lower or equal to 0")
    distribution = Exponential(rate=rate)
    # Values are generated by using a truncated uniform distribution and
    # then using the inverse CDF for the Exponential distribution.
    # Get upper and lower CDF values
    u = distribution.cdf(max_value)
    return distribution.icdf(torch.rand(rate.shape, generator=generator).mul(u)).clamp(
        max=max_value
    )


def rand_trunc_half_cauchy(
    size: list[int] | tuple[int, ...],
    scale: float = 1.0,
    max_value: float = 4.0,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a truncated
    half-Cauchy distribution.

    Args:
    ----
        size (list or tuple): Specifies the tensor shape.
        scale (float, optional): Specifies the scale of the
            half-Cauchy distribution. Default: ``1.0``
        max_value (float, optional): Specifies the maximum value.
            Default: ``4.0``
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from a
            truncated half-Cauchy distribution.

    Raises:
    ------
        ValueError if the ``max_value`` parameter is not valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import rand_trunc_half_cauchy
        >>> rand_trunc_half_cauchy((2, 3), scale=1.0, max_value=3.0)  # doctest:+ELLIPSIS
        tensor([[...]])
    """
    if max_value <= 0:
        raise ValueError(f"`max_value` has to be greater than 0 (received: {max_value})")
    distribution = HalfCauchy(scale=scale)
    # Values are generated by using a truncated uniform distribution and
    # then using the inverse CDF for the Cauchy distribution.
    # Get upper CDF value
    u = distribution.cdf(torch.tensor(max_value))
    return distribution.icdf(rand_uniform(size, low=0.0, high=u, generator=generator)).clamp(
        max=max_value
    )


def trunc_half_cauchy(
    scale: Tensor,
    max_value: Tensor,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a truncated
    half-Cauchy distribution.

    Args:
    ----
        scale (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the scale
            of the half-Cauchy distribution.
        max_value (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the maximum value.
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from
            a truncated Cauchy distribution

    Raises:
    ------
        ValueError if the ``scale`` and ``max_value`` parameter are
            not valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import trunc_half_cauchy
        >>> trunc_half_cauchy(
        ...     scale=torch.tensor([1.0, 3.0, 5.0]),
        ...     max_value=torch.tensor([5.0, 10.0, 15.0]),
        ... )  # doctest:+ELLIPSIS
        tensor([...])
    """
    if scale.shape != max_value.shape:
        raise ValueError(
            "Incorrect shapes. The shapes of all the input tensors must be equal:  "
            f"scale={scale.shape}  max_value={max_value.shape}"
        )
    if torch.any(scale <= 0.0):
        raise ValueError("All the `scale` values have to be greater than 0")
    if torch.any(max_value <= 0.0):
        raise ValueError("Found at least one value in `max_value` that is lower or equal to 0")
    distribution = HalfCauchy(scale=scale)
    # Values are generated by using a truncated uniform distribution and
    # then using the inverse CDF for the Cauchy distribution.
    # Get upper CDF value
    u = distribution.cdf(max_value)
    return distribution.icdf(torch.rand(scale.shape, generator=generator).mul(u)).clamp(
        max=max_value
    )


def rand_trunc_half_normal(
    size: list[int] | tuple[int, ...],
    std: float = 1.0,
    max_value: float = 5.0,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a truncated
    half-Normal distribution.

    Args:
    ----
        size (list or tuple): Specifies the tensor shape.
        std (float, optional): Specifies the standard deviation of
            the half-Normal distribution. Default: ``1.0``
        max_value (float, optional): Specifies the maximum value.
            Default: ``5.0``
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from a
            truncated half-Normal distribution.

    Raises:
    ------
        ValueError if the ``max_value`` parameter is not valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import rand_trunc_half_normal
        >>> rand_trunc_half_normal((2, 3), std=1.0, max_value=3.0)  # doctest:+ELLIPSIS
        tensor([[...]])
    """
    if max_value <= 0:
        raise ValueError(f"`max_value` has to be greater than 0 (received: {max_value})")
    distribution = HalfNormal(scale=std)
    # Values are generated by using a truncated uniform distribution and
    # then using the inverse CDF for the Normal distribution.
    # Get upper cdf value
    u = distribution.cdf(torch.tensor(max_value))
    return distribution.icdf(rand_uniform(size, low=0.0, high=u, generator=generator)).clamp(
        max=max_value
    )


def trunc_half_normal(
    std: Tensor,
    max_value: Tensor,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a truncated
    half-Normal distribution.

    Args:
    ----
        std (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the standard deviation
            of the half-Normal distribution.
        max_value (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the maximum value.
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from a
            truncated half-Normal distribution.

    Raises:
    ------
        ValueError if the ``std`` and ``max_value`` parameters are not
            valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import trunc_half_normal
        >>> trunc_half_normal(
        ...     std=torch.tensor([1.0, 3.0, 5.0]), max_value=torch.tensor([5.0, 10.0, 15.0])
        ... )  # doctest:+ELLIPSIS
        tensor([...])
    """
    if std.shape != max_value.shape:
        raise ValueError(
            "Incorrect shapes. The shapes of all the input tensors must be equal: "
            f"std={std.shape}  max_value={max_value.shape}"
        )
    if torch.any(std <= 0.0):
        raise ValueError("All the `std` values have to be greater than 0")
    if torch.any(max_value <= 0.0):
        raise ValueError("All the `max_value` values must be greater than 0")
    distribution = HalfNormal(scale=std)
    # Values are generated by using a uniform distribution and
    # then using the inverse CDF for the Normal distribution.
    # Get upper and lower CDF values
    u = distribution.cdf(max_value)
    return distribution.icdf(torch.rand(std.shape, generator=generator).mul(u)).clamp(max=max_value)


def rand_trunc_log_normal(
    size: list[int] | tuple[int, ...],
    mean: float = 0.0,
    std: float = 1.0,
    min_value: float = 0.0,
    max_value: float = 5.0,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a truncated log-
    Normal distribution.

    Args:
    ----
        size (list or tuple): Specifies the tensor shape.
        mean (float, optional): Specifies the mean of the underlying
            Normal distribution. Default: ``0.0``
        std (float, optional): Specifies the standard deviation of
            the underlying Normal distribution. Default: ``1.0``
        min_value (float, optional): Specifies the minimum value.
            Default: ``0.0``
        max_value (float, optional): Specifies the maximum value.
            Default: ``5.0``
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from a
            truncated log-Normal distribution.

    Raises:
    ------
        ValueError if the ``min_value`` and ``max_value`` parameters
            are not valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import rand_trunc_log_normal
        >>> rand_trunc_log_normal(
        ...     (2, 3), mean=0.0, std=1.0, min_value=1.0, max_value=4.0
        ... )  # doctest:+ELLIPSIS
        tensor([[...]])
    """
    if max_value < min_value:
        raise ValueError(
            f"`max_value` ({max_value}) has to be greater or equal to `min_value` ({min_value})"
        )
    distribution = LogNormal(loc=mean, scale=std)
    # Values are generated by using a truncated uniform distribution and
    # then using the inverse CDF for the log-Normal distribution.
    # Get upper and lower CDF values
    lo, up = distribution.cdf(torch.tensor([min_value, max_value]))
    return distribution.icdf(rand_uniform(size, low=lo, high=up, generator=generator)).clamp(
        min=min_value, max=max_value
    )


def trunc_log_normal(
    mean: Tensor,
    std: Tensor,
    min_value: Tensor,
    max_value: Tensor,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a truncated log-
    Normal distribution.

    Args:
    ----
        mean (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the mean of the
            underlying Normal distribution.
        std (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the standard deviation
            of the underlying Normal distribution.
        min_value (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the minimum value.
        max_value (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the maximum value.
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from a
            truncated log-Normal distribution.

    Raises:
    ------
        ValueError if the ``mean``, ``std``, ``min_value`` and
            ``max_value`` parameters are not valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import trunc_log_normal
        >>> trunc_log_normal(
        ...     mean=torch.tensor([-1.0, 0.0, 1.0]),
        ...     std=torch.tensor([1.0, 3.0, 5.0]),
        ...     min_value=torch.tensor([0.0, 1.0, 2.0]),
        ...     max_value=torch.tensor([5.0, 10.0, 15.0]),
        ... )  # doctest:+ELLIPSIS
        tensor([...])
    """
    if not shapes_are_equal((mean, std, min_value, max_value)):
        raise ValueError(
            "Incorrect shapes. The shapes of all the input tensors must be equal: "
            f"mean={mean.shape}  std={std.shape}  min_value={min_value.shape}  "
            f"max_value={max_value.shape}"
        )
    if torch.any(std <= 0.0):
        raise ValueError("All the `std` values have to be greater than 0")
    if torch.any(max_value < min_value):
        raise ValueError(
            "Found at least one value in `min_value` that is higher than its associated "
            "`max_value`"
        )
    distribution = LogNormal(loc=mean, scale=std)
    # Values are generated by using a uniform distribution and
    # then using the inverse CDF for the log-Normal distribution.
    # Get upper and lower CDF values
    lo, up = distribution.cdf(torch.stack([min_value, max_value]))
    return distribution.icdf(uniform(low=lo, high=up, generator=generator)).clamp(
        min=min_value, max=max_value
    )


def rand_trunc_normal(
    size: list[int] | tuple[int, ...],
    mean: float = 0.0,
    std: float = 1.0,
    min_value: float = -3.0,
    max_value: float = 3.0,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a truncated
    Normal distribution.

    Args:
    ----
        size (list or tuple): Specifies the tensor shape.
        mean (float, optional): Specifies the mean of the Normal
            distribution. Default: ``0.0``
        std (float, optional): Specifies the standard deviation of
            the Normal distribution. Default: ``1.0``
        min_value (float, optional): Specifies the minimum value.
            Default: ``-3.0``
        max_value (float, optional): Specifies the maximum value.
            Default: ``3.0``
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from a
            truncated Normal distribution.

    Raises:
    ------
        ValueError if the ``min_value`` and  ``max_value`` parameters
            are not valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import rand_trunc_normal
        >>> rand_trunc_normal(
        ...     (2, 3), mean=1.0, std=2.0, min_value=-5.0, max_value=5.0
        ... )  # doctest:+ELLIPSIS
        tensor([[...]])
    """
    if max_value < min_value:
        raise ValueError(
            f"`max_value` ({max_value}) has to be greater or equal to `min_value` ({min_value})"
        )
    distribution = Normal(loc=mean, scale=std)
    # Values are generated by using a truncated uniform distribution and
    # then using the inverse CDF for the Normal distribution.
    # Get upper and lower cdf values
    lo, up = distribution.cdf(torch.tensor([min_value, max_value]))
    return distribution.icdf(rand_uniform(size, low=lo, high=up, generator=generator)).clamp(
        min=min_value, max=max_value
    )


def trunc_normal(
    mean: Tensor,
    std: Tensor,
    min_value: Tensor,
    max_value: Tensor,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a truncated
    Normal distribution.

    Args:
    ----
        mean (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the mean of the
            Normal distribution.
        std (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the standard deviation
            of the Normal distribution.
        min_value (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the minimum value.
        max_value (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the maximum value.
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from a
            truncated Normal distribution.

    Raises:
    ------
        ValueError if the ``min_value`` and  ``max_value`` parameters
            are not valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import trunc_normal
        >>> trunc_normal(
        ...     mean=torch.tensor([1.0, 0.0, -1.0]),
        ...     std=torch.tensor([1.0, 3.0, 5.0]),
        ...     min_value=torch.tensor([-5.0, -10.0, -15.0]),
        ...     max_value=torch.tensor([5.0, 10.0, 15.0]),
        ... )  # doctest:+ELLIPSIS
        tensor([...])
    """
    if not shapes_are_equal((mean, std, min_value, max_value)):
        raise ValueError(
            "Incorrect shapes. The shapes of all the input tensors must be equal: "
            f"mean={mean.shape}  std={std.shape}  min_value={min_value.shape}  "
            f"max_value={max_value.shape}"
        )
    if torch.any(std <= 0.0):
        raise ValueError("All the `std` values have to be greater than 0")
    if torch.any(max_value < min_value):
        raise ValueError(
            "Found at least one value in `min_value` that is higher than its associated "
            "`max_value`"
        )
    distribution = Normal(loc=mean, scale=std)
    # Values are generated by using a uniform distribution and
    # then using the inverse CDF for the Normal distribution.
    # Get upper and lower CDF values
    lo, up = distribution.cdf(torch.stack([min_value, max_value]))
    return distribution.icdf(uniform(low=lo, high=up, generator=generator)).clamp(
        min=min_value, max=max_value
    )


def rand_uniform(
    size: list[int] | tuple[int, ...],
    low: float = 0.0,
    high: float = 1.0,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a uniform
    distribution.

    Args:
    ----
        size (list or tuple): Specifies the tensor shape.
        low (float, optional): Specifies the minimum value
            (inclusive). Default: ``0.0``
        high (float, optional): Specifies the maximum value
            (exclusive). Default: ``1.0``
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from a
            uniform distribution.

    Raises:
    ------
        ValueError if the ``low`` and  ``high`` parameters  are not
            valid.

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import rand_uniform
        >>> rand_uniform((2, 3), low=-1.0, high=2.0)  # doctest:+ELLIPSIS
        tensor([[...]])
    """
    if high < low:
        raise ValueError(f"`high` ({high}) has to be greater or equal to `low` ({low})")
    return (
        torch.rand(size=size, generator=generator).mul(high - low).add(low).clamp(min=low, max=high)
    )


def uniform(low: Tensor, high: Tensor, generator: torch.Generator | None = None) -> Tensor:
    r"""Creates a tensor filled with values sampled from a uniform
    distribution.

    Unlike ``rand_uniform``, this function allows to sample values
    from different uniform distributions at the same time.
    The shape of the ``low`` and ``high`` tensors are used to infer
    the output size.

    Args:
    ----
        low (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the minimum values
            (inclusive).
        high (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the maximum values
            (exclusive).
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``: A tensor filled with values sampled
            from a uniform distribution where the minimum and maximum
            values are given as input.

    Raises:
        ValueError if the input tensor shapes do not match or if at
            least one value in ``low`` tensor is higher than its
            associated high value in ``high``

    Example usage:

    .. code-block:: pycon

        >>> import torch
        >>> from startorch.random import uniform
        >>> uniform(
        ...     low=torch.tensor([-1.0, 0.0, 1.0]), high=torch.tensor([1.0, 3.0, 5.0])
        ... )  # doctest:+ELLIPSIS
        tensor([...])
    """
    if low.shape != high.shape:
        raise ValueError(
            f"Incorrect shapes. The shapes of all the input tensors must be equal: "
            f"low={low.shape}  high={high.shape})"
        )
    if torch.any(high < low):
        raise ValueError(
            "Found at least one value in `low` that is higher than its associated "
            "value in `high`.`uniform` expects to return a [low, high) range"
        )
    return (
        torch.rand(size=high.shape, generator=generator)
        .mul(high - low)
        .add(low)
        .clamp(min=low, max=high)
    )


def rand_log_uniform(
    size: list[int] | tuple[int, ...],
    low: float,
    high: float,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a uniform
    distribution in the log space.

    Args:
    ----
        size (list or tuple): Specifies the tensor shape.
        low (float): Specifies the minimum value (inclusive).
            This value needs to be positive.
        high (float): Specifies the maximum value (exclusive).
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor``: A tensor filled with values sampled from a
            uniform distribution in the log space.

    Raises:
    ------
        ValueError if the ``low`` and  ``high`` parameters  are not
            valid.

    Example usage:

    .. code-block:: pycon

        >>> from startorch.random import rand_log_uniform
        >>> rand_log_uniform((2, 3), low=0.1, high=1000.0)  # doctest:+ELLIPSIS
        tensor([[...]])
    """
    if high < low:
        raise ValueError(f"`high` ({high}) has to be greater or equal to `low` ({low})")
    log_low = math.log(low)
    return (
        torch.rand(size=size, generator=generator)
        .mul(math.log(high) - log_low)
        .add(log_low)
        .exp()
        .clamp(min=low, max=high)
    )


def log_uniform(low: Tensor, high: Tensor, generator: torch.Generator | None = None) -> Tensor:
    r"""Creates a tensor filled with values sampled from a uniform
    distribution in the log space.

    Args:
    ----
        low (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the minimum values
            (inclusive).
        high (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the maximum values
            (exclusive).
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
    -------
        ``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``: A tensor filled with values sampled
            from a uniform distribution in the log space where the
            minimum and maximum values are given as input.

    Raises:
    ------
        ValueError if the ``low`` and  ``high`` parameters  are not
            valid.

    Example usage:

    .. code-block:: pycon

        >>> from startorch.random import log_uniform
        >>> log_uniform(
        ...     low=torch.tensor([0.01, 0.1, 1.0]), high=torch.tensor([1.0, 10.0, 100.0])
        ... )  # doctest:+ELLIPSIS
        tensor([...])
    """
    if low.shape != high.shape:
        raise ValueError(
            "Incorrect shapes. The shapes of all the input tensors must be equal: "
            f"low={low.shape}  high={high.shape}"
        )
    if torch.any(high < low):
        raise ValueError(
            "Found at least one value in `low` that is higher than its associated "
            "value in `high`. `log_uniform` expects to return a [low, high) range"
        )
    log_low = low.log()
    return (
        torch.rand(size=high.shape, generator=generator)
        .mul(high.log() - log_low)
        .add(log_low)
        .exp()
        .clamp(min=low, max=high)
    )


def rand_asinh_uniform(
    size: list[int] | tuple[int, ...],
    low: float,
    high: float,
    generator: torch.Generator | None = None,
) -> Tensor:
    r"""Creates a tensor filled with values sampled from a uniform
    distribution in the inverse hyperbolic sine space.

    Args:
        size (list or tuple): Specifies the tensor shape.
        low (float): Specifies the minimum value (inclusive).
            This value needs to be positive.
        high (float): Specifies the maximum value (exclusive).
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
        ``torch.Tensor``: A tensor filled with values sampled from a
            uniform distribution in the inverse hyperbolic sine space.

    Raises:
    ------
        ValueError if the ``low`` and  ``high`` parameters  are not
            valid.

    Example usage:

    .. code-block:: pycon

        >>> from startorch.random import rand_asinh_uniform
        >>> rand_asinh_uniform((2, 3), low=-1000.0, high=1000.0)  # doctest:+ELLIPSIS
        tensor([[...]])
    """
    if high < low:
        raise ValueError(f"`high` ({high}) has to be greater or equal to `low` ({low})")
    log_low = math.asinh(low)
    return (
        torch.rand(size=size, generator=generator)
        .mul(math.asinh(high) - log_low)
        .add(log_low)
        .sinh()
        .clamp(min=low, max=high)
    )


def asinh_uniform(low: Tensor, high: Tensor, generator: torch.Generator | None = None) -> Tensor:
    r"""Creates a tensor filled with values sampled from a uniform
    distribution in the inverse hyperbolic sine space.

    Args:
        low (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the minimum values
            (inclusive).
        high (``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``): Specifies the maximum values
            (exclusive).
        generator (``torch.Generator`` or None, optional): Specifies
            an optional random generator. Default: ``None``

    Returns:
        ``torch.Tensor`` of type float and shape
            ``(d0, d1, ..., dn)``: A tensor filled with values sampled
            from a uniform distribution in the inverse hyperbolic sine
            space where the minimum and maximum values are given as
            input.

    Raises:
    ------
        ValueError if the ``low`` and  ``high`` parameters  are not
            valid.

    Example usage:

    .. code-block:: pycon

        >>> from startorch.random import asinh_uniform
        >>> asinh_uniform(
        ...     low=torch.tensor([-10.0, 0.0, 1.0]),
        ...     high=torch.tensor([1.0, 10.0, 100.0]),
        ... )  # doctest:+ELLIPSIS
        tensor([...])
    """
    if low.shape != high.shape:
        raise ValueError(
            "Incorrect shapes. The shapes of all the input tensors must be equal: "
            f"low={low.shape}  high={high.shape}"
        )
    if torch.any(high < low):
        raise ValueError(
            "Found at least one value in `low` that is higher than its associated "
            "value in `high`. `asinh_uniform` expects to return a [low, high) range"
        )
    log_low = low.asinh()
    return (
        torch.rand(size=high.shape, generator=generator)
        .mul(high.asinh() - log_low)
        .add(log_low)
        .sinh()
        .clamp(min=low, max=high)
    )
