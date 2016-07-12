// This file is part of Eigen, a lightweight C++ template library
// for linear algebra.
//
// Copyright (C) 2010-2012 Gael Guennebaud <gael.guennebaud@inria.fr>
// Copyright (C) 2010 Benoit Jacob <jacob.benoit.1@gmail.com>
//
// This Source Code Form is subject to the terms of the Mozilla
// Public License v. 2.0. If a copy of the MPL was not distributed
// with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

#ifndef EIGEN_GLOBAL_FUNCTIONS_H
#define EIGEN_GLOBAL_FUNCTIONS_H

#define EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(NAME,FUNCTOR) \
  template<typename Derived> \
  inline const Eigen::CwiseUnaryOp<Eigen::internal::FUNCTOR<typename Derived::Scalar>, const Derived> \
  (NAME)(const Eigen::ArrayBase<Derived>& x) { \
    return Eigen::CwiseUnaryOp<Eigen::internal::FUNCTOR<typename Derived::Scalar>, const Derived>(x.derived()); \
  }

#define EIGEN_ARRAY_DECLARE_GLOBAL_EIGEN_UNARY(NAME,FUNCTOR) \
  \
  template<typename Derived> \
  struct NAME##_retval<ArrayBase<Derived> > \
  { \
    typedef const Eigen::CwiseUnaryOp<Eigen::internal::FUNCTOR<typename Derived::Scalar>, const Derived> type; \
  }; \
  template<typename Derived> \
  struct NAME##_impl<ArrayBase<Derived> > \
  { \
    static inline typename NAME##_retval<ArrayBase<Derived> >::type run(const Eigen::ArrayBase<Derived>& x) \
    { \
      return typename NAME##_retval<ArrayBase<Derived> >::type(x.derived()); \
    } \
  };

namespace Eigen
{
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(real,scalar_real_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(imag,scalar_imag_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(conj,scalar_conjugate_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(inverse,scalar_inverse_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(sin,scalar_sin_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(cos,scalar_cos_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(tan,scalar_tan_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(atan,scalar_atan_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(asin,scalar_asin_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(acos,scalar_acos_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(sinh,scalar_sinh_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(cosh,scalar_cosh_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(tanh,scalar_tanh_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(lgamma,scalar_lgamma_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(digamma,scalar_digamma_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(erf,scalar_erf_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(erfc,scalar_erfc_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(exp,scalar_exp_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(log,scalar_log_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(log10,scalar_log10_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(abs,scalar_abs_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(abs2,scalar_abs2_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(arg,scalar_arg_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(sqrt,scalar_sqrt_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(square,scalar_square_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(cube,scalar_cube_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(round,scalar_round_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(floor,scalar_floor_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(ceil,scalar_ceil_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(isnan,scalar_isnan_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(isinf,scalar_isinf_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(isfinite,scalar_isfinite_op)
  EIGEN_ARRAY_DECLARE_GLOBAL_UNARY(sign,scalar_sign_op)
  
  template<typename Derived>
  inline const Eigen::CwiseUnaryOp<Eigen::internal::scalar_pow_op<typename Derived::Scalar>, const Derived>
  pow(const Eigen::ArrayBase<Derived>& x, const typename Derived::Scalar& exponent) {
    return x.derived().pow(exponent);
  }

  /** \returns an expression of the coefficient-wise power of \a x to the given array of \a exponents.
    *
    * This function computes the coefficient-wise power.
    *
    * Example: \include Cwise_array_power_array.cpp
    * Output: \verbinclude Cwise_array_power_array.out
    * 
    * \sa ArrayBase::pow()
    */
  template<typename Derived,typename ExponentDerived>
  inline const Eigen::CwiseBinaryOp<Eigen::internal::scalar_binary_pow_op<typename Derived::Scalar, typename ExponentDerived::Scalar>, const Derived, const ExponentDerived>
  pow(const Eigen::ArrayBase<Derived>& x, const Eigen::ArrayBase<ExponentDerived>& exponents) 
  {
    return Eigen::CwiseBinaryOp<Eigen::internal::scalar_binary_pow_op<typename Derived::Scalar, typename ExponentDerived::Scalar>, const Derived, const ExponentDerived>(
      x.derived(),
      exponents.derived()
    );
  }
  
  /** \returns an expression of the coefficient-wise power of the scalar \a x to the given array of \a exponents.
    *
    * This function computes the coefficient-wise power between a scalar and an array of exponents.
    * Beaware that the scalar type of the input scalar \a x and the exponents \a exponents must be the same.
    *
    * Example: \include Cwise_scalar_power_array.cpp
    * Output: \verbinclude Cwise_scalar_power_array.out
    * 
    * \sa ArrayBase::pow()
    */
  template<typename Derived>
  inline const Eigen::CwiseBinaryOp<Eigen::internal::scalar_binary_pow_op<typename Derived::Scalar, typename Derived::Scalar>, const typename Derived::ConstantReturnType, const Derived>
  pow(const typename Derived::Scalar& x, const Eigen::ArrayBase<Derived>& exponents) 
  {
    typename Derived::ConstantReturnType constant_x(exponents.rows(), exponents.cols(), x);
    return Eigen::CwiseBinaryOp<Eigen::internal::scalar_binary_pow_op<typename Derived::Scalar, typename Derived::Scalar>, const typename Derived::ConstantReturnType, const Derived>(
      constant_x,
      exponents.derived()
    );
  }
  
  /**
    * \brief Component-wise division of a scalar by array elements.
    **/
  template <typename Derived>
  inline const Eigen::CwiseUnaryOp<Eigen::internal::scalar_inverse_mult_op<typename Derived::Scalar>, const Derived>
    operator/(const typename Derived::Scalar& s, const Eigen::ArrayBase<Derived>& a)
  {
    return Eigen::CwiseUnaryOp<Eigen::internal::scalar_inverse_mult_op<typename Derived::Scalar>, const Derived>(
      a.derived(),
      Eigen::internal::scalar_inverse_mult_op<typename Derived::Scalar>(s)  
    );
  }

  /** \cpp11 \returns an expression of the coefficient-wise igamma(\a a, \a x) to the given arrays.
    *
    * This function computes the coefficient-wise incomplete gamma function.
    *
    * \note This function supports only float and double scalar types in c++11 mode. To support other scalar types,
    * or float/double in non c++11 mode, the user has to provide implementations of igammac(T,T) for any scalar
    * type T to be supported.
    *
    * \sa Eigen::igammac(), Eigen::lgamma()
    */
  template<typename Derived,typename ExponentDerived>
  inline const Eigen::CwiseBinaryOp<Eigen::internal::scalar_igamma_op<typename Derived::Scalar>, const Derived, const ExponentDerived>
  igamma(const Eigen::ArrayBase<Derived>& a, const Eigen::ArrayBase<ExponentDerived>& x) 
  {
    return Eigen::CwiseBinaryOp<Eigen::internal::scalar_igamma_op<typename Derived::Scalar>, const Derived, const ExponentDerived>(
      a.derived(),
      x.derived()
    );
  }

  /** \cpp11 \returns an expression of the coefficient-wise igammac(\a a, \a x) to the given arrays.
    *
    * This function computes the coefficient-wise complementary incomplete gamma function.
    *
    * \note This function supports only float and double scalar types in c++11 mode. To support other scalar types,
    * or float/double in non c++11 mode, the user has to provide implementations of igammac(T,T) for any scalar
    * type T to be supported.
    *
    * \sa Eigen::igamma(), Eigen::lgamma()
    */
  template<typename Derived,typename ExponentDerived>
  inline const Eigen::CwiseBinaryOp<Eigen::internal::scalar_igammac_op<typename Derived::Scalar>, const Derived, const ExponentDerived>
  igammac(const Eigen::ArrayBase<Derived>& a, const Eigen::ArrayBase<ExponentDerived>& x) 
  {
    return Eigen::CwiseBinaryOp<Eigen::internal::scalar_igammac_op<typename Derived::Scalar>, const Derived, const ExponentDerived>(
      a.derived(),
      x.derived()
    );
  }

  /** \cpp11 \returns an expression of the coefficient-wise polygamma(\a n, \a x) to the given arrays.
    *
    * It returns the \a n -th derivative of the digamma(psi) evaluated at \c x.
    *
    * \note This function supports only float and double scalar types in c++11 mode. To support other scalar types,
    * or float/double in non c++11 mode, the user has to provide implementations of polygamma(T,T) for any scalar
    * type T to be supported.
    *
    * \sa Eigen::digamma()
    */
  // * \warning Be careful with the order of the parameters: x.polygamma(n) is equivalent to polygamma(n,x)
  // * \sa ArrayBase::polygamma()
  template<typename DerivedN,typename DerivedX>
  inline const Eigen::CwiseBinaryOp<Eigen::internal::scalar_polygamma_op<typename DerivedX::Scalar>, const DerivedN, const DerivedX>
  polygamma(const Eigen::ArrayBase<DerivedN>& n, const Eigen::ArrayBase<DerivedX>& x)
  {
    return Eigen::CwiseBinaryOp<Eigen::internal::scalar_polygamma_op<typename DerivedX::Scalar>, const DerivedN, const DerivedX>(
      n.derived(),
      x.derived()
    );
  }

  /** \returns an expression of the coefficient-wise zeta(\a x, \a q) to the given arrays.
    *
    * It returns the Riemann zeta function of two arguments \a x and \a q:
    *
    * \param x is the exposent, it must be > 1
    * \param q is the shift, it must be > 0
    *
    * \note This function supports only float and double scalar types. To support other scalar types, the user has
    * to provide implementations of zeta(T,T) for any scalar type T to be supported.
    *
    * \sa ArrayBase::zeta()
    */
  template<typename DerivedX,typename DerivedQ>
  inline const Eigen::CwiseBinaryOp<Eigen::internal::scalar_zeta_op<typename DerivedX::Scalar>, const DerivedX, const DerivedQ>
  zeta(const Eigen::ArrayBase<DerivedX>& x, const Eigen::ArrayBase<DerivedQ>& q)
  {
    return Eigen::CwiseBinaryOp<Eigen::internal::scalar_zeta_op<typename DerivedX::Scalar>, const DerivedX, const DerivedQ>(
      x.derived(),
      q.derived()
    );
  }

  namespace internal
  {
    EIGEN_ARRAY_DECLARE_GLOBAL_EIGEN_UNARY(real,scalar_real_op)
    EIGEN_ARRAY_DECLARE_GLOBAL_EIGEN_UNARY(imag,scalar_imag_op)
    EIGEN_ARRAY_DECLARE_GLOBAL_EIGEN_UNARY(abs2,scalar_abs2_op)
  }
}

// TODO: cleanly disable those functions that are not supported on Array (numext::real_ref, internal::random, internal::isApprox...)

#endif // EIGEN_GLOBAL_FUNCTIONS_H
