class Refiner(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  mode : str
  sample_pixels : int
  threshold : float
  prevent_oversampling : bool
  conv1 : __torch__.torch.nn.modules.conv.___torch_mangle_56.Conv2d
  bn1 : __torch__.torch.nn.modules.batchnorm.___torch_mangle_57.BatchNorm2d
  conv2 : __torch__.torch.nn.modules.conv.___torch_mangle_58.Conv2d
  bn2 : __torch__.torch.nn.modules.batchnorm.___torch_mangle_59.BatchNorm2d
  conv3 : __torch__.torch.nn.modules.conv.___torch_mangle_60.Conv2d
  bn3 : __torch__.torch.nn.modules.batchnorm.___torch_mangle_61.BatchNorm2d
  conv4 : __torch__.torch.nn.modules.conv.___torch_mangle_62.Conv2d
  relu : __torch__.torch.nn.modules.activation.ReLU
  kernel_size : Final[int] = 3
  def forward(self: __torch__.model.refiner.Refiner,
    src: Tensor,
    bgr: Tensor,
    pha: Tensor,
    fgr: Tensor,
    err: Tensor,
    hid: Tensor) -> Tuple[Tensor, Tensor, Tensor]:
    _0 = __torch__.torch.nn.functional.___torch_mangle_63.interpolate
    _1 = torch.slice(torch.size(src), 2, 9223372036854775807, 1)
    H_full, W_full, = _1
    H_half = torch.floordiv(H_full, 2)
    W_half = torch.floordiv(W_full, 2)
    H_quat = torch.floordiv(H_full, 4)
    W_quat = torch.floordiv(W_full, 4)
    src_bgr = torch.cat([src, bgr], 1)
    if torch.ne(self.mode, "full"):
      ref0 = (self).select_area(err, (H_quat, W_quat), )
      ref_idx = torch.nonzero(torch.squeeze(ref0, 1))
      _2 = torch.slice(ref_idx, 0, 0, 9223372036854775807, 1)
      bat = torch.select(_2, 1, 0)
      _3 = torch.slice(ref_idx, 0, 0, 9223372036854775807, 1)
      row = torch.select(_3, 1, 1)
      _4 = torch.slice(ref_idx, 0, 0, 9223372036854775807, 1)
      col = torch.select(_4, 1, 2)
      if torch.ne(torch.len(ref_idx), 0):
        x = torch.cat([hid, pha, fgr], 1)
        x0 = _0(x, [H_half, W_half], None, "bilinear", False, None, )
        _5 = __torch__.torch.nn.functional._pad(x0, [3, 3, 3, 3], "constant", 0., )
        _6 = torch.unfold(torch.permute(_5, [0, 2, 3, 1]), 1, 8, 2)
        _7 = torch.unfold(_6, 2, 8, 2)
        _8 = annotate(List[Optional[Tensor]], [bat, row, col])
        x1 = torch.index(_7, _8)
        y = _0(src_bgr, [H_half, W_half], None, "bilinear", False, None, )
        _9 = __torch__.torch.nn.functional._pad(y, [3, 3, 3, 3], "constant", 0., )
        _10 = torch.unfold(torch.permute(_9, [0, 2, 3, 1]), 1, 8, 2)
        _11 = torch.unfold(_10, 2, 8, 2)
        _12 = annotate(List[Optional[Tensor]], [bat, row, col])
        y0 = torch.index(_11, _12)
        x2 = (self.conv1).forward(torch.cat([x1, y0], 1), )
        x3 = (self.bn1).forward(x2, )
        x4 = (self.relu).forward(x3, )
        x5 = (self.conv2).forward(x4, )
        x6 = (self.bn2).forward(x5, )
        x7 = (self.relu).forward(x6, )
        x8 = _0(x7, [8, 8], None, "nearest", None, None, )
        _13 = __torch__.torch.nn.functional._pad(src_bgr, [2, 2, 2, 2], "constant", 0., )
        _14 = torch.permute(_13, [0, 2, 3, 1])
        _15 = torch.unfold(torch.unfold(_14, 1, 8, 4), 2, 8, 4)
        _16 = annotate(List[Optional[Tensor]], [bat, row, col])
        y1 = torch.index(_15, _16)
        x9 = (self.conv3).forward(torch.cat([x8, y1], 1), )
        x10 = (self.bn3).forward(x9, )
        x11 = (self.relu).forward(x10, )
        x12 = (self.conv4).forward(x11, )
        pha2 = _0(pha, [H_full, W_full], None, "bilinear", False, None, )
        _17 = torch.permute(pha2, [0, 2, 3, 1])
        pha3 = torch.unfold(torch.unfold(_17, 1, 4, 4), 2, 4, 4)
        _18 = torch.slice(x12, 0, 0, 9223372036854775807, 1)
        _19 = torch.slice(_18, 1, 0, 1, 1)
        _20 = annotate(List[Optional[Tensor]], [bat, row, col])
        _21 = torch.index_put_(pha3, _20, _19, False)
        _22 = torch.permute(pha3, [0, 3, 1, 4, 2, 5])
        _23 = [torch.size(pha3, 0), 1, H_full, W_full]
        pha4 = torch.view(_22, _23)
        fgr2 = _0(fgr, [H_full, W_full], None, "bilinear", False, None, )
        _24 = torch.permute(fgr2, [0, 2, 3, 1])
        fgr3 = torch.unfold(torch.unfold(_24, 1, 4, 4), 2, 4, 4)
        _25 = torch.slice(x12, 0, 0, 9223372036854775807, 1)
        _26 = torch.slice(_25, 1, 1, 9223372036854775807, 1)
        _27 = annotate(List[Optional[Tensor]], [bat, row, col])
        _28 = torch.index_put_(fgr3, _27, _26, False)
        _29 = torch.permute(fgr3, [0, 3, 1, 4, 2, 5])
        _30 = [torch.size(fgr3, 0), 3, H_full, W_full]
        pha1, fgr1 = pha4, torch.view(_29, _30)
      else:
        pha5 = _0(pha, [H_full, W_full], None, "bilinear", False, None, )
        fgr4 = _0(fgr, [H_full, W_full], None, "bilinear", False, None, )
        pha1, fgr1 = pha5, fgr4
      pha0, fgr0, ref = pha1, fgr1, ref0
    else:
      x13 = torch.cat([hid, pha, fgr], 1)
      x14 = _0(x13, [H_half, W_half], None, "bilinear", False, None, )
      y2 = _0(src_bgr, [H_half, W_half], None, "bilinear", False, None, )
      x15 = __torch__.torch.nn.functional._pad(x14, [3, 3, 3, 3], "constant", 0., )
      y3 = __torch__.torch.nn.functional._pad(y2, [3, 3, 3, 3], "constant", 0., )
      x16 = (self.conv1).forward(torch.cat([x15, y3], 1), )
      x17 = (self.bn1).forward(x16, )
      x18 = (self.relu).forward(x17, )
      x19 = (self.conv2).forward(x18, )
      x20 = (self.bn2).forward(x19, )
      x21 = (self.relu).forward(x20, )
      _31 = [torch.add(H_full, 4), torch.add(W_full, 4)]
      x22 = _0(x21, _31, None, "nearest", None, None, )
      y4 = __torch__.torch.nn.functional._pad(src_bgr, [2, 2, 2, 2], "constant", 0., )
      x23 = (self.conv3).forward(torch.cat([x22, y4], 1), )
      x24 = (self.bn3).forward(x23, )
      x25 = (self.relu).forward(x24, )
      x26 = (self.conv4).forward(x25, )
      _32 = torch.slice(x26, 0, 0, 9223372036854775807, 1)
      pha6 = torch.slice(_32, 1, 0, 1, 1)
      _33 = torch.slice(x26, 0, 0, 9223372036854775807, 1)
      fgr5 = torch.slice(_33, 1, 1, 9223372036854775807, 1)
      _34 = torch.size(src, 0)
      _35 = ops.prim.device(src)
      _36 = ops.prim.dtype(src)
      ref1 = torch.ones([_34, 1, H_quat, W_quat], dtype=_36, layout=None, device=_35, pin_memory=None)
      pha0, fgr0, ref = pha6, fgr5, ref1
    return (pha0, fgr0, ref)
  def select_area(self: __torch__.model.refiner.Refiner,
    err: Tensor,
    quat_size: Tuple[int, int]) -> Tensor:
    _37 = __torch__.torch.nn.functional.___torch_mangle_63.interpolate
    _38 = torch.slice(torch.size(err), 2, 9223372036854775807, 1)
    _39, _40, = quat_size
    if torch.ne(_38, [_39, _40]):
      _41, _42, = quat_size
      err1 = _37(err, [_41, _42], None, "bilinear", False, None, )
      err0 = err1
    else:
      err0 = err
    if torch.eq(self.mode, "sampling"):
      err2 = torch.view(err0, [torch.size(err0, 0), -1])
      _43 = torch.floordiv(self.sample_pixels, 16)
      _44, _45 = torch.topk(err2, _43, -1, True, False)
      ref2 = torch.zeros_like(err2, dtype=None, layout=None, device=None, pin_memory=None, memory_format=None)
      _46 = torch.scatter_(ref2, 1, _45, 1)
      if self.prevent_oversampling:
        _47 = torch.masked_fill_(ref2, torch.eq(err2, 0), 0)
      else:
        pass
      _48 = torch.size(err2, 0)
      _49, _50, = quat_size
      ref3 = torch.view(ref2, [_48, 1, _49, _50])
      ref = ref3
    else:
      ref = torch.gt(err0, self.threshold)
    return ref
