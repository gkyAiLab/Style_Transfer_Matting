def interpolate(input: Tensor,
    size: Optional[List[int]]=None,
    scale_factor: Optional[List[float]]=None,
    mode: str="nearest",
    align_corners: Optional[bool]=None,
    recompute_scale_factor: Optional[bool]=None) -> Tensor:
  _0 = "align_corners option can only be set with the interpolating modes: linear | bilinear | bicubic | trilinear"
  _1 = "Default upsampling behavior when mode={} is changed to align_corners=False since 0.4.0. Please specify align_corners=True if the old behavior is desired. See the documentation of nn.Upsample for details."
  _2 = "only one of size or scale_factor should be defined"
  _3 = "size shape must match input shape. Input is {}D, size is {}"
  _4 = "scale_factor shape must match input shape. Input is {}D, scale_factor is {}"
  _5 = "either size or scale_factor should be defined"
  _6 = "The default behavior for interpolate/upsample with float scale_factor changed in 1.6.0 to align with other frameworks/libraries, and now uses scale_factor directly, instead of relying on the computed output size. If you wish to restore the old behavior, please set recompute_scale_factor=True. See the documentation of nn.Upsample for details. "
  _7 = "recompute_scale_factor is not meaningful with an explicit size."
  _8 = __torch__.torch.nn.functional.adaptive_avg_pool2d
  _9 = __torch__.torch.nn.functional.adaptive_avg_pool3d
  _10 = "Got 3D input, but bilinear mode needs 4D input"
  _11 = "Got 3D input, but trilinear mode needs 5D input"
  _12 = "Got 4D input, but linear mode needs 3D input"
  _13 = "Got 4D input, but trilinear mode needs 5D input"
  _14 = "Got 5D input, but linear mode needs 3D input"
  _15 = "Got 5D input, but bilinear mode needs 4D input"
  _16 = "Input Error: Only 3D, 4D and 5D input Tensors supported (got {}D) for the modes: nearest | linear | bilinear | bicubic | trilinear (got {})"
  _17 = uninitialized(Tensor)
  _18 = uninitialized(List[int])
  _19 = uninitialized(None)
  _20 = uninitialized(List[float])
  _21 = uninitialized(Optional[List[int]])
  _22 = uninitialized(Optional[List[float]])
  _23 = uninitialized(Optional[List[int]])
  _24 = uninitialized(Optional[bool])
  _25 = uninitialized(bool)
  _26 = torch.__contains__(["nearest", "area"], mode)
  if _26:
    _27 = torch.__isnot__(align_corners, None)
    if _27:
      ops.prim.RaiseException(_0)
      align_corners1 = _24
    else:
      align_corners1 = align_corners
    align_corners0 = align_corners1
  else:
    if torch.__is__(align_corners, None):
      torch.warn(torch.format(_1, mode), 2)
      align_corners2 = False
    else:
      align_corners3 = unchecked_cast(bool, align_corners)
      align_corners2 = align_corners3
    align_corners0 = align_corners2
  dim = torch.sub(torch.dim(input), 2)
  if torch.__isnot__(size, None):
    size1 = unchecked_cast(List[int], size)
    _28, size0 = torch.__isnot__(scale_factor, None), size1
  else:
    _28, size0 = False, size
  if _28:
    ops.prim.RaiseException(_2)
    scale_factors, size2, output_size = _22, _23, _21
  else:
    if torch.__isnot__(size0, None):
      size4 = unchecked_cast(List[int], size0)
      if torch.__is__(scale_factor, None):
        pass
      else:
        ops.prim.RaiseException("AssertionError: ")
      if torch.ne(torch.len(size4), dim):
        _29 = torch.format(_3, dim, torch.len(size4))
        ops.prim.RaiseException(_29)
      else:
        pass
      scale_factors0, size3, output_size0 = None, size4, size4
    else:
      _30 = torch.__isnot__(scale_factor, None)
      if _30:
        scale_factor0 = unchecked_cast(List[float], scale_factor)
        if torch.__is__(size0, None):
          size6 = size0
        else:
          ops.prim.RaiseException("AssertionError: ")
          size6 = _23
        _31 = torch.ne(torch.len(scale_factor0), dim)
        if _31:
          _32 = torch.format(_4, dim, torch.len(scale_factor0))
          ops.prim.RaiseException(_32)
        else:
          pass
        scale_factors1, size5, output_size1 = scale_factor0, size6, None
      else:
        ops.prim.RaiseException(_5)
        scale_factors1, size5, output_size1 = _20, _23, _19
      scale_factors0, size3, output_size0 = scale_factors1, size5, output_size1
    scale_factors, size2, output_size = scale_factors0, size3, output_size0
  _33 = torch.__is__(recompute_scale_factor, None)
  if _33:
    _34 = torch.__isnot__(scale_factors, None)
    if _34:
      scale_factors4 = unchecked_cast(List[float], scale_factors)
      _35 = torch.len(scale_factors4)
      _36 = 0
      _37 = torch.gt(_35, 0)
      while _37:
        scale = scale_factors4[_36]
        _38 = torch.ne(torch.floor(scale), scale)
        if _38:
          torch.warn(_6, 2)
          _39 = False
        else:
          _39 = True
        _40 = torch.add(_36, 1)
        _41 = torch.__and__(torch.lt(_40, _35), _39)
        _37, _36 = _41, _40
      scale_factors3 = scale_factors4
    else:
      scale_factors3 = scale_factors
    recompute_scale_factor0, scale_factors2 = recompute_scale_factor, scale_factors3
  else:
    recompute_scale_factor1 = unchecked_cast(bool, recompute_scale_factor)
    if recompute_scale_factor1:
      _42 = torch.__isnot__(size2, None)
    else:
      _42 = False
    if _42:
      ops.prim.RaiseException(_7)
    else:
      pass
    recompute_scale_factor0, scale_factors2 = recompute_scale_factor1, scale_factors
  if torch.eq(mode, "area"):
    _43 = torch.__is__(output_size, None)
  else:
    _43 = False
  if _43:
    recompute_scale_factor2 = True
  else:
    recompute_scale_factor2 = recompute_scale_factor0
  _44 = torch.__isnot__(recompute_scale_factor2, None)
  if _44:
    recompute_scale_factor3 = unchecked_cast(bool, recompute_scale_factor2)
    _45 = recompute_scale_factor3
  else:
    _45 = False
  if _45:
    _46 = torch.__isnot__(scale_factors2, None)
    if _46:
      scale_factors7 = unchecked_cast(List[float], scale_factors2)
      scale_factors6 = scale_factors7
    else:
      ops.prim.RaiseException("AssertionError: ")
      scale_factors6 = _20
    output_size3 = annotate(List[int], [])
    for i in range(dim):
      _47 = torch.size(input, torch.add(i, 2))
      _48 = torch.mul(float(_47), scale_factors6[i])
      _49 = torch.append(output_size3, torch.floor(_48))
    output_size2, scale_factors5 = output_size3, None
  else:
    output_size2, scale_factors5 = output_size, scale_factors2
  if torch.eq(torch.dim(input), 3):
    _50 = torch.eq(mode, "nearest")
  else:
    _50 = False
  if _50:
    _52 = torch.upsample_nearest1d(input, output_size2, scale_factors5)
    _51 = _52
  else:
    if torch.eq(torch.dim(input), 4):
      _53 = torch.eq(mode, "nearest")
    else:
      _53 = False
    if _53:
      _55 = torch.upsample_nearest2d(input, output_size2, scale_factors5)
      _54 = _55
    else:
      if torch.eq(torch.dim(input), 5):
        _56 = torch.eq(mode, "nearest")
      else:
        _56 = False
      if _56:
        _58 = torch.upsample_nearest3d(input, output_size2, scale_factors5)
        _57 = _58
      else:
        if torch.eq(torch.dim(input), 3):
          _59 = torch.eq(mode, "area")
        else:
          _59 = False
        if _59:
          _61 = torch.__isnot__(output_size2, None)
          if _61:
            output_size5 = unchecked_cast(List[int], output_size2)
            output_size4 = output_size5
          else:
            ops.prim.RaiseException("AssertionError: ")
            output_size4 = _18
          _62 = torch.adaptive_avg_pool1d(input, output_size4)
          _60 = _62
        else:
          if torch.eq(torch.dim(input), 4):
            _63 = torch.eq(mode, "area")
          else:
            _63 = False
          if _63:
            _65 = torch.__isnot__(output_size2, None)
            if _65:
              output_size7 = unchecked_cast(List[int], output_size2)
              output_size6 = output_size7
            else:
              ops.prim.RaiseException("AssertionError: ")
              output_size6 = _18
            _64 = _8(input, output_size6, )
          else:
            _66 = torch.eq(torch.dim(input), 5)
            if _66:
              _67 = torch.eq(mode, "area")
            else:
              _67 = False
            if _67:
              _69 = torch.__isnot__(output_size2, None)
              if _69:
                output_size9 = unchecked_cast(List[int], output_size2)
                output_size8 = output_size9
              else:
                ops.prim.RaiseException("AssertionError: ")
                output_size8 = _18
              _68 = _9(input, output_size8, )
            else:
              _70 = torch.eq(torch.dim(input), 3)
              if _70:
                _72 = torch.eq(mode, "linear")
                _71 = _72
              else:
                _71 = False
              if _71:
                _74 = torch.__isnot__(align_corners0, None)
                if _74:
                  align_corners5 = unchecked_cast(bool, align_corners0)
                  align_corners4 = align_corners5
                else:
                  ops.prim.RaiseException("AssertionError: ")
                  align_corners4 = _25
                _75 = torch.upsample_linear1d(input, output_size2, align_corners4, scale_factors5)
                _73 = _75
              else:
                _76 = torch.eq(torch.dim(input), 4)
                if _76:
                  _78 = torch.eq(mode, "bilinear")
                  _77 = _78
                else:
                  _77 = False
                if _77:
                  _80 = torch.__isnot__(align_corners0, None)
                  if _80:
                    align_corners7 = unchecked_cast(bool, align_corners0)
                    align_corners6 = align_corners7
                  else:
                    ops.prim.RaiseException("AssertionError: ")
                    align_corners6 = _25
                  _81 = torch.upsample_bilinear2d(input, output_size2, align_corners6, scale_factors5)
                  _79 = _81
                else:
                  _82 = torch.eq(torch.dim(input), 5)
                  if _82:
                    _84 = torch.eq(mode, "trilinear")
                    _83 = _84
                  else:
                    _83 = False
                  if _83:
                    _86 = torch.__isnot__(align_corners0, None)
                    if _86:
                      align_corners9 = unchecked_cast(bool, align_corners0)
                      align_corners8 = align_corners9
                    else:
                      ops.prim.RaiseException("AssertionError: ")
                      align_corners8 = _25
                    _87 = torch.upsample_trilinear3d(input, output_size2, align_corners8, scale_factors5)
                    _85 = _87
                  else:
                    _88 = torch.eq(torch.dim(input), 4)
                    if _88:
                      _90 = torch.eq(mode, "bicubic")
                      _89 = _90
                    else:
                      _89 = False
                    if _89:
                      _92 = torch.__isnot__(align_corners0, None)
                      if _92:
                        align_corners11 = unchecked_cast(bool, align_corners0)
                        align_corners10 = align_corners11
                      else:
                        ops.prim.RaiseException("AssertionError: ")
                        align_corners10 = _25
                      _93 = torch.upsample_bicubic2d(input, output_size2, align_corners10, scale_factors5)
                      _91 = _93
                    else:
                      _94 = torch.eq(torch.dim(input), 3)
                      if _94:
                        _96 = torch.eq(mode, "bilinear")
                        _95 = _96
                      else:
                        _95 = False
                      if _95:
                        ops.prim.RaiseException(_10)
                      else:
                        pass
                      _97 = torch.eq(torch.dim(input), 3)
                      if _97:
                        _99 = torch.eq(mode, "trilinear")
                        _98 = _99
                      else:
                        _98 = False
                      if _98:
                        ops.prim.RaiseException(_11)
                      else:
                        pass
                      _100 = torch.eq(torch.dim(input), 4)
                      if _100:
                        _102 = torch.eq(mode, "linear")
                        _101 = _102
                      else:
                        _101 = False
                      if _101:
                        ops.prim.RaiseException(_12)
                      else:
                        pass
                      _103 = torch.eq(torch.dim(input), 4)
                      if _103:
                        _105 = torch.eq(mode, "trilinear")
                        _104 = _105
                      else:
                        _104 = False
                      if _104:
                        ops.prim.RaiseException(_13)
                      else:
                        pass
                      _106 = torch.eq(torch.dim(input), 5)
                      if _106:
                        _108 = torch.eq(mode, "linear")
                        _107 = _108
                      else:
                        _107 = False
                      if _107:
                        ops.prim.RaiseException(_14)
                      else:
                        pass
                      _109 = torch.eq(torch.dim(input), 5)
                      if _109:
                        _111 = torch.eq(mode, "bilinear")
                        _110 = _111
                      else:
                        _110 = False
                      if _110:
                        ops.prim.RaiseException(_15)
                      else:
                        pass
                      _112 = torch.format(_16, torch.dim(input), mode)
                      ops.prim.RaiseException(_112)
                      _91 = _17
                    _85 = _91
                  _79 = _85
                _73 = _79
              _68 = _73
            _64 = _68
          _60 = _64
        _57 = _60
      _54 = _57
    _51 = _54
  return _51
