class ASPP(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  convs : __torch__.torch.nn.modules.container.ModuleList
  project : __torch__.torch.nn.modules.container.___torch_mangle_50.Sequential
  def forward(self: __torch__.torchvision.models.segmentation.deeplabv3.ASPP,
    x: Tensor) -> Tensor:
    res = annotate(List[Tensor], [])
    _0 = self.convs
    _1 = getattr(_0, "0")
    _2 = getattr(_0, "1")
    _3 = getattr(_0, "2")
    _4 = getattr(_0, "3")
    _5 = getattr(_0, "4")
    _6 = torch.append(res, (_1).forward(x, ))
    _7 = torch.append(res, (_2).forward(x, ))
    _8 = torch.append(res, (_3).forward(x, ))
    _9 = torch.append(res, (_4).forward(x, ))
    _10 = torch.append(res, (_5).forward(x, ))
    res0 = torch.cat(res, 1)
    return (self.project).forward(res0, )
class ASPPConv(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  __annotations__["0"] = __torch__.torch.nn.modules.conv.___torch_mangle_44.Conv2d
  __annotations__["1"] = __torch__.torch.nn.modules.batchnorm.___torch_mangle_3.BatchNorm2d
  __annotations__["2"] = __torch__.torch.nn.modules.activation.___torch_mangle_42.ReLU
  def forward(self: __torch__.torchvision.models.segmentation.deeplabv3.ASPPConv,
    input: Tensor) -> Tensor:
    _11 = getattr(self, "0")
    _12 = getattr(self, "1")
    _13 = getattr(self, "2")
    input0 = (_11).forward(input, )
    input1 = (_12).forward(input0, )
    return (_13).forward(input1, )
  def __len__(self: __torch__.torchvision.models.segmentation.deeplabv3.ASPPConv) -> int:
    return 3
class ASPPPooling(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  __annotations__["0"] = __torch__.torch.nn.modules.pooling.AdaptiveAvgPool2d
  __annotations__["1"] = __torch__.torch.nn.modules.conv.___torch_mangle_41.Conv2d
  __annotations__["2"] = __torch__.torch.nn.modules.batchnorm.___torch_mangle_3.BatchNorm2d
  __annotations__["3"] = __torch__.torch.nn.modules.activation.___torch_mangle_42.ReLU
  def forward(self: __torch__.torchvision.models.segmentation.deeplabv3.ASPPPooling,
    x: Tensor) -> Tensor:
    _14 = __torch__.torch.nn.functional.___torch_mangle_63.interpolate
    size = torch.slice(torch.size(x), -2, 9223372036854775807, 1)
    _15 = getattr(self, "0")
    _16 = getattr(self, "1")
    _17 = getattr(self, "2")
    _18 = getattr(self, "3")
    x0 = (_15).forward(x, )
    x1 = (_16).forward(x0, )
    x2 = (_17).forward(x1, )
    x3 = (_18).forward(x2, )
    _19 = _14(x3, size, None, "bilinear", False, None, )
    return _19
  def __len__(self: __torch__.torchvision.models.segmentation.deeplabv3.ASPPPooling) -> int:
    return 4
