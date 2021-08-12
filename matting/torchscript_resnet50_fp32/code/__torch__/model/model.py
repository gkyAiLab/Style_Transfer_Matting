class MattingRefine(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  backbone_scale : float
  refine_mode : str
  refine_sample_pixels : int
  refine_threshold : float
  refine_prevent_oversampling : bool
  backbone : __torch__.model.resnet.ResNetEncoder
  aspp : __torch__.torchvision.models.segmentation.deeplabv3.ASPP
  decoder : __torch__.model.decoder.Decoder
  refiner : __torch__.model.refiner.Refiner
  def forward(self: __torch__.model.model.MattingRefine,
    src: Tensor,
    bgr: Tensor) -> Tuple[Tensor, Tensor, Tensor, Tensor, Tensor, Tensor]:
    _0 = "AssertionError: src and bgr must have the same shape"
    _1 = "AssertionError: src and bgr must have width and height that are divisible by 4"
    _2 = __torch__.torch.nn.functional.___torch_mangle_64.interpolate
    _3 = torch.eq(torch.size(src), torch.size(bgr))
    if _3:
      pass
    else:
      ops.prim.RaiseException(_0)
    _4 = torch.floordiv(torch.size(src, 2), 4)
    _5 = torch.eq(torch.mul(_4, 4), torch.size(src, 2))
    if _5:
      _7 = torch.floordiv(torch.size(src, 3), 4)
      _8 = torch.eq(torch.mul(_7, 4), torch.size(src, 3))
      _6 = _8
    else:
      _6 = False
    if _6:
      pass
    else:
      ops.prim.RaiseException(_1)
    src_sm = _2(src, None, self.backbone_scale, "bilinear", False, True, )
    bgr_sm = _2(bgr, None, self.backbone_scale, "bilinear", False, True, )
    x = torch.cat([src_sm, bgr_sm], 1)
    x0, _9, _10, _11, _12, = (self.backbone).forward(x, )
    x1 = (self.aspp).forward(x0, )
    x2 = (self.decoder).forward(x1, _9, _10, _11, _12, )
    _13 = torch.slice(x2, 0, 0, 9223372036854775807, 1)
    pha_sm = torch.clamp_(torch.slice(_13, 1, 0, 1, 1), 0, 1)
    _14 = torch.slice(x2, 0, 0, 9223372036854775807, 1)
    fgr_sm = torch.slice(_14, 1, 1, 4, 1)
    _15 = torch.slice(x2, 0, 0, 9223372036854775807, 1)
    err_sm = torch.clamp_(torch.slice(_15, 1, 4, 5, 1), 0, 1)
    _16 = torch.slice(x2, 0, 0, 9223372036854775807, 1)
    _17 = torch.slice(_16, 1, 5, 9223372036854775807, 1)
    hid_sm = torch.relu_(_17)
    self.refiner.mode = self.refine_mode
    self.refiner.sample_pixels = self.refine_sample_pixels
    self.refiner.threshold = self.refine_threshold
    self.refiner.prevent_oversampling = self.refine_prevent_oversampling
    _18 = (self.refiner).forward(src, bgr, pha_sm, fgr_sm, err_sm, hid_sm, )
    pha, fgr, ref_sm, = _18
    pha0 = torch.clamp_(pha, 0, 1)
    fgr0 = torch.clamp_(torch.add_(fgr, src, alpha=1), 0, 1)
    fgr_sm0 = torch.clamp_(torch.add_(src_sm, fgr_sm, alpha=1), 0, 1)
    _19 = (pha0, fgr0, pha_sm, fgr_sm0, err_sm, ref_sm)
    return _19
