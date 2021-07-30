def batch_norm(input: Tensor,
    running_mean: Optional[Tensor],
    running_var: Optional[Tensor],
    weight: Optional[Tensor]=None,
    bias: Optional[Tensor]=None,
    training: bool=False,
    momentum: float=0.10000000000000001,
    eps: float=1.0000000000000001e-05) -> Tensor:
  _0 = __torch__.torch.nn.functional._verify_batch_size
  if training:
    _1 = _0(torch.size(input), )
  else:
    pass
  _2 = torch.batch_norm(input, weight, bias, running_mean, running_var, training, momentum, eps, True)
  return _2
def relu(input: Tensor,
    inplace: bool=False) -> Tensor:
  if inplace:
    result = torch.relu_(input)
  else:
    result = torch.relu(input)
  return result
def _max_pool2d(input: Tensor,
    kernel_size: List[int],
    stride: Optional[List[int]]=None,
    padding: List[int]=[0, 0],
    dilation: List[int]=[1, 1],
    ceil_mode: bool=False,
    return_indices: bool=False) -> Tensor:
  if torch.__is__(stride, None):
    stride0 = annotate(List[int], [])
  else:
    stride0 = unchecked_cast(List[int], stride)
  _3 = torch.max_pool2d(input, kernel_size, stride0, padding, dilation, ceil_mode)
  return _3
def adaptive_avg_pool2d(input: Tensor,
    output_size: List[int]) -> Tensor:
  _4 = torch.gt(torch.len(torch.size(input)), torch.len(output_size))
  if _4:
    pass
  else:
    ops.prim.RaiseException("AssertionError: ")
  _5 = torch.adaptive_avg_pool2d(input, output_size)
  return _5
def dropout(input: Tensor,
    p: float=0.5,
    training: bool=True,
    inplace: bool=False) -> Tensor:
  _6 = "dropout probability has to be between 0 and 1, but got {}"
  if torch.lt(p, 0.):
    _7 = True
  else:
    _7 = torch.gt(p, 1.)
  if _7:
    ops.prim.RaiseException(torch.format(_6, p))
  else:
    pass
  if inplace:
    _8 = torch.dropout_(input, p, training)
  else:
    _8 = torch.dropout(input, p, training)
  return _8
def _pad(input: Tensor,
    pad: List[int],
    mode: str="constant",
    value: float=0.) -> Tensor:
  _9 = "AssertionError: Padding length must be divisible by 2"
  _10 = "AssertionError: Padding length too large"
  _11 = "Padding mode \"{}\"\" doesn\'t take in value argument"
  _12 = "AssertionError: 3D tensors expect 2 values for padding"
  _13 = __torch__.torch.nn.functional._pad_circular
  _14 = "AssertionError: 4D tensors expect 4 values for padding"
  _15 = "AssertionError: 5D tensors expect 6 values for padding"
  _16 = "Only 3D, 4D, 5D padding with non-constant padding are supported for now"
  _17 = uninitialized(Tensor)
  _18 = torch.eq(torch.remainder(torch.len(pad), 2), 0)
  if _18:
    pass
  else:
    ops.prim.RaiseException(_9)
  _19 = torch.le(torch.floordiv(torch.len(pad), 2), torch.dim(input))
  if _19:
    pass
  else:
    ops.prim.RaiseException(_10)
  if torch.eq(mode, "constant"):
    _21 = torch.constant_pad_nd(input, pad, value)
    _20 = _21
  else:
    if torch.eq(value, 0):
      pass
    else:
      _22 = torch.add("AssertionError: ", torch.format(_11, mode))
      ops.prim.RaiseException(_22)
    if torch.eq(torch.dim(input), 3):
      if torch.eq(torch.len(pad), 2):
        pass
      else:
        ops.prim.RaiseException(_12)
      if torch.eq(mode, "reflect"):
        _25 = torch.reflection_pad1d(input, pad)
        _24 = _25
      else:
        if torch.eq(mode, "replicate"):
          _27 = torch.replication_pad1d(input, pad)
          _26 = _27
        else:
          if torch.eq(mode, "circular"):
            _28 = _13(input, pad, )
          else:
            ops.prim.RaiseException("")
            _28 = _17
          _26 = _28
        _24 = _26
      _23 = _24
    else:
      if torch.eq(torch.dim(input), 4):
        if torch.eq(torch.len(pad), 4):
          pass
        else:
          ops.prim.RaiseException(_14)
        if torch.eq(mode, "reflect"):
          _31 = torch.reflection_pad2d(input, pad)
          _30 = _31
        else:
          if torch.eq(mode, "replicate"):
            _33 = torch.replication_pad2d(input, pad)
            _32 = _33
          else:
            if torch.eq(mode, "circular"):
              _34 = _13(input, pad, )
            else:
              ops.prim.RaiseException("")
              _34 = _17
            _32 = _34
          _30 = _32
        _29 = _30
      else:
        if torch.eq(torch.dim(input), 5):
          if torch.eq(torch.len(pad), 6):
            pass
          else:
            ops.prim.RaiseException(_15)
          if torch.eq(mode, "reflect"):
            ops.prim.RaiseException("")
            _36 = _17
          else:
            if torch.eq(mode, "replicate"):
              _38 = torch.replication_pad3d(input, pad)
              _37 = _38
            else:
              _39 = torch.eq(mode, "circular")
              if _39:
                _40 = _13(input, pad, )
              else:
                ops.prim.RaiseException("")
                _40 = _17
              _37 = _40
            _36 = _37
          _35 = _36
        else:
          ops.prim.RaiseException(_16)
          _35 = _17
        _29 = _35
      _23 = _29
    _20 = _23
  return _20
def adaptive_avg_pool3d(input: Tensor,
    output_size: List[int]) -> Tensor:
  _41 = torch.gt(torch.len(torch.size(input)), torch.len(output_size))
  if _41:
    pass
  else:
    ops.prim.RaiseException("AssertionError: ")
  _42 = torch.adaptive_avg_pool3d(input, output_size)
  return _42
def _verify_batch_size(size: List[int]) -> None:
  _43 = "Expected more than 1 value per channel when training, got input size {}"
  size_prods = size[0]
  size_prods0 = size_prods
  for i in range(torch.sub(torch.len(size), 2)):
    size_prods1 = torch.mul(size_prods0, size[torch.add(i, 2)])
    size_prods0 = size_prods1
  if torch.eq(size_prods0, 1):
    ops.prim.RaiseException(torch.format(_43, size))
  else:
    pass
  return None
def _pad_circular(input: Tensor,
    padding: List[int]) -> Tensor:
  _44 = "AssertionError: Padding value causes wrapping around more than once."
  _45 = "AssertionError: Negative padding value is resulting in an empty dimension."
  in_shape = torch.size(input)
  paddable_shape = torch.slice(in_shape, 2, 9223372036854775807, 1)
  ndim = torch.len(paddable_shape)
  _46 = [9223372036854775807, torch.len(paddable_shape)]
  for idx in range(ops.prim.min(_46)):
    size = paddable_shape[idx]
    _47 = torch.neg(torch.add(torch.mul(idx, 2), 1))
    if torch.le(padding[_47], size):
      pass
    else:
      ops.prim.RaiseException(_44)
    _48 = torch.neg(torch.add(torch.mul(idx, 2), 2))
    if torch.le(padding[_48], size):
      pass
    else:
      ops.prim.RaiseException(_44)
    _49 = torch.neg(torch.add(torch.mul(idx, 2), 1))
    _50 = padding[_49]
    _51 = torch.neg(torch.add(torch.mul(idx, 2), 2))
    _52 = torch.add(torch.add(_50, padding[_51]), size)
    if torch.ge(_52, 0):
      pass
    else:
      ops.prim.RaiseException(_45)
  out_shape = torch.slice(in_shape, 0, 2, 1)
  _53 = [9223372036854775807, torch.len(paddable_shape)]
  out_shape0 = out_shape
  for idx0 in range(ops.prim.min(_53)):
    size0 = paddable_shape[idx0]
    _54 = torch.neg(torch.add(torch.mul(idx0, 2), 1))
    _55 = torch.add(size0, padding[_54])
    _56 = torch.neg(torch.add(torch.mul(idx0, 2), 2))
    out_shape1 = torch.add_(out_shape0, [torch.add(_55, padding[_56])])
    out_shape0 = out_shape1
  out = torch.empty(out_shape0, dtype=ops.prim.dtype(input), layout=ops.prim.layout(input), device=ops.prim.device(input), pin_memory=None, memory_format=None)
  if torch.eq(ndim, 1):
    out_d0 = ops.prim.max(padding[-2], 0)
    out_d1 = torch.sub(out_shape0[2], ops.prim.max(padding[-1], 0))
    in_d0 = ops.prim.max(torch.neg(padding[-2]), 0)
    _57 = in_shape[2]
    _58 = ops.prim.max(torch.neg(padding[-1]), 0)
    in_d1 = torch.sub(_57, _58)
    _59 = torch.slice(input, -1, in_d0, in_d1, 1)
    _60 = torch.slice(out, -1, out_d0, out_d1, 1)
    _61 = torch.copy_(_60, _59, False)
  else:
    if torch.eq(ndim, 2):
      out_d00 = ops.prim.max(padding[-2], 0)
      out_d10 = torch.sub(out_shape0[2], ops.prim.max(padding[-1], 0))
      out_h0 = ops.prim.max(padding[-4], 0)
      out_h1 = torch.sub(out_shape0[3], ops.prim.max(padding[-3], 0))
      in_d00 = ops.prim.max(torch.neg(padding[-2]), 0)
      _62 = in_shape[2]
      _63 = ops.prim.max(torch.neg(padding[-1]), 0)
      in_d10 = torch.sub(_62, _63)
      in_h0 = ops.prim.max(torch.neg(padding[-4]), 0)
      _64 = in_shape[3]
      _65 = ops.prim.max(torch.neg(padding[-3]), 0)
      in_h1 = torch.sub(_64, _65)
      _66 = torch.slice(input, -2, in_d00, in_d10, 1)
      _67 = torch.slice(_66, -1, in_h0, in_h1, 1)
      _68 = torch.slice(out, -2, out_d00, out_d10, 1)
      _69 = torch.slice(_68, -1, out_h0, out_h1, 1)
      _70 = torch.copy_(_69, _67, False)
    else:
      if torch.eq(ndim, 3):
        out_d01 = ops.prim.max(padding[-2], 0)
        out_d11 = torch.sub(out_shape0[2], ops.prim.max(padding[-1], 0))
        out_h00 = ops.prim.max(padding[-4], 0)
        out_h10 = torch.sub(out_shape0[3], ops.prim.max(padding[-3], 0))
        out_w0 = ops.prim.max(padding[-6], 0)
        out_w1 = torch.sub(out_shape0[4], ops.prim.max(padding[-5], 0))
        in_d01 = ops.prim.max(torch.neg(padding[-2]), 0)
        _71 = in_shape[2]
        _72 = ops.prim.max(torch.neg(padding[-1]), 0)
        in_d11 = torch.sub(_71, _72)
        in_h00 = ops.prim.max(torch.neg(padding[-4]), 0)
        _73 = in_shape[3]
        _74 = ops.prim.max(torch.neg(padding[-3]), 0)
        in_h10 = torch.sub(_73, _74)
        in_w0 = ops.prim.max(torch.neg(padding[-6]), 0)
        _75 = in_shape[4]
        _76 = ops.prim.max(torch.neg(padding[-5]), 0)
        in_w1 = torch.sub(_75, _76)
        _77 = torch.slice(input, -3, in_d01, in_d11, 1)
        _78 = torch.slice(_77, -2, in_h00, in_h10, 1)
        _79 = torch.slice(_78, -1, in_w0, in_w1, 1)
        _80 = torch.slice(out, -3, out_d01, out_d11, 1)
        _81 = torch.slice(_80, -2, out_h00, out_h10, 1)
        _82 = torch.slice(_81, -1, out_w0, out_w1, 1)
        _83 = torch.copy_(_82, _79, False)
      else:
        pass
  if torch.gt(padding[-2], 0):
    _84 = torch.sub(out_shape0[2], padding[-2])
    i0 = torch.sub(_84, ops.prim.max(padding[-1], 0))
    i1 = torch.sub(out_shape0[2], ops.prim.max(padding[-1], 0))
    o1 = padding[-2]
    _85 = torch.slice(out, 0, 0, 9223372036854775807, 1)
    _86 = torch.slice(_85, 1, 0, 9223372036854775807, 1)
    _87 = torch.slice(_86, 2, i0, i1, 1)
    _88 = torch.slice(out, 0, 0, 9223372036854775807, 1)
    _89 = torch.slice(_88, 1, 0, 9223372036854775807, 1)
    _90 = torch.copy_(torch.slice(_89, 2, 0, o1, 1), _87, False)
  else:
    pass
  if torch.gt(padding[-1], 0):
    i00 = ops.prim.max(padding[-2], 0)
    i10 = torch.add(ops.prim.max(padding[-2], 0), padding[-1])
    o0 = torch.sub(out_shape0[2], padding[-1])
    o10 = out_shape0[2]
    _91 = torch.slice(out, 0, 0, 9223372036854775807, 1)
    _92 = torch.slice(_91, 1, 0, 9223372036854775807, 1)
    _93 = torch.slice(_92, 2, i00, i10, 1)
    _94 = torch.slice(out, 0, 0, 9223372036854775807, 1)
    _95 = torch.slice(_94, 1, 0, 9223372036854775807, 1)
    _96 = torch.copy_(torch.slice(_95, 2, o0, o10, 1), _93, False)
  else:
    pass
  if torch.gt(torch.len(padding), 2):
    if torch.gt(padding[-4], 0):
      _97 = torch.sub(out_shape0[3], padding[-4])
      i01 = torch.sub(_97, ops.prim.max(padding[-3], 0))
      i11 = torch.sub(out_shape0[3], ops.prim.max(padding[-3], 0))
      o11 = padding[-4]
      _98 = torch.slice(out, 0, 0, 9223372036854775807, 1)
      _99 = torch.slice(_98, 1, 0, 9223372036854775807, 1)
      _100 = torch.slice(_99, 2, 0, 9223372036854775807, 1)
      _101 = torch.slice(_100, 3, i01, i11, 1)
      _102 = torch.slice(out, 0, 0, 9223372036854775807, 1)
      _103 = torch.slice(_102, 1, 0, 9223372036854775807, 1)
      _104 = torch.slice(_103, 2, 0, 9223372036854775807, 1)
      _105 = torch.copy_(torch.slice(_104, 3, 0, o11, 1), _101, False)
    else:
      pass
    if torch.gt(padding[-3], 0):
      i02 = ops.prim.max(padding[-4], 0)
      i12 = torch.add(ops.prim.max(padding[-4], 0), padding[-3])
      o00 = torch.sub(out_shape0[3], padding[-3])
      o12 = out_shape0[3]
      _106 = torch.slice(out, 0, 0, 9223372036854775807, 1)
      _107 = torch.slice(_106, 1, 0, 9223372036854775807, 1)
      _108 = torch.slice(_107, 2, 0, 9223372036854775807, 1)
      _109 = torch.slice(_108, 3, i02, i12, 1)
      _110 = torch.slice(out, 0, 0, 9223372036854775807, 1)
      _111 = torch.slice(_110, 1, 0, 9223372036854775807, 1)
      _112 = torch.slice(_111, 2, 0, 9223372036854775807, 1)
      _113 = torch.copy_(torch.slice(_112, 3, o00, o12, 1), _109, False)
    else:
      pass
  else:
    pass
  if torch.gt(torch.len(padding), 4):
    if torch.gt(padding[-6], 0):
      _114 = torch.sub(out_shape0[4], padding[-6])
      i03 = torch.sub(_114, ops.prim.max(padding[-5], 0))
      i13 = torch.sub(out_shape0[4], ops.prim.max(padding[-5], 0))
      o13 = padding[-6]
      _115 = torch.slice(out, 0, 0, 9223372036854775807, 1)
      _116 = torch.slice(_115, 1, 0, 9223372036854775807, 1)
      _117 = torch.slice(_116, 2, 0, 9223372036854775807, 1)
      _118 = torch.slice(_117, 3, 0, 9223372036854775807, 1)
      _119 = torch.slice(_118, 4, i03, i13, 1)
      _120 = torch.slice(out, 0, 0, 9223372036854775807, 1)
      _121 = torch.slice(_120, 1, 0, 9223372036854775807, 1)
      _122 = torch.slice(_121, 2, 0, 9223372036854775807, 1)
      _123 = torch.slice(_122, 3, 0, 9223372036854775807, 1)
      _124 = torch.copy_(torch.slice(_123, 4, 0, o13, 1), _119, False)
    else:
      pass
    if torch.gt(padding[-5], 0):
      i04 = ops.prim.max(padding[-6], 0)
      i14 = torch.add(ops.prim.max(padding[-6], 0), padding[-5])
      o01 = torch.sub(out_shape0[4], padding[-5])
      o14 = out_shape0[4]
      _125 = torch.slice(out, 0, 0, 9223372036854775807, 1)
      _126 = torch.slice(_125, 1, 0, 9223372036854775807, 1)
      _127 = torch.slice(_126, 2, 0, 9223372036854775807, 1)
      _128 = torch.slice(_127, 3, 0, 9223372036854775807, 1)
      _129 = torch.slice(_128, 4, i04, i14, 1)
      _130 = torch.slice(out, 0, 0, 9223372036854775807, 1)
      _131 = torch.slice(_130, 1, 0, 9223372036854775807, 1)
      _132 = torch.slice(_131, 2, 0, 9223372036854775807, 1)
      _133 = torch.slice(_132, 3, 0, 9223372036854775807, 1)
      _134 = torch.copy_(torch.slice(_133, 4, o01, o14, 1), _129, False)
    else:
      pass
  else:
    pass
  return out
