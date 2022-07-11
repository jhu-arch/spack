# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvd(RPackage):
    """Functions for Extreme Value Distributions.

    Extends simulation, distribution, quantile and density functions to
    univariate and multivariate parametric extreme value distributions, and
    provides fitting functions which calculate maximum likelihood estimates for
    univariate and bivariate maxima models, and for univariate and bivariate
    threshold models."""

    cran = "evd"

    version('2.3-6', sha256='8edb8bc4f06d246c4343fd923bb5d5df99724d6db8821bfd996220343a834cb6')
    version('2.3-3', sha256='2fc5ef2e0c3a2a9392425ddd45914445497433d90fb80b8c363877baee4559b4')
