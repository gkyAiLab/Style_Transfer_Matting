class Sequential(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  __annotations__["0"] = __torch__.torch.nn.modules.conv.___torch_mangle_2.Conv2d
  __annotations__["1"] = __torch__.torch.nn.modules.batchnorm.___torch_mangle_3.BatchNorm2d
  def forward(self: __torch__.torch.nn.modules.container.Sequential,
    input: Tensor) -> Tensor:
    _0 = getattr(self, "0")
    _1 = getattr(self, "1")
    input0 = (_0).forward(input, )
    return (_1).forward(input0, )
  def __len__(self: __torch__.torch.nn.modules.container.Sequential) -> int:
    return 2
class ModuleList(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  __annotations__["0"] = __torch__.torch.nn.modules.container.___torch_mangle_43.Sequential
  __annotations__["1"] = __torch__.torchvision.models.segmentation.deeplabv3.ASPPConv
  __annotations__["2"] = __torch__.torchvision.models.segmentation.deeplabv3.___torch_mangle_46.ASPPConv
  __annotations__["3"] = __torch__.torchvision.models.segmentation.deeplabv3.___torch_mangle_48.ASPPConv
  __annotations__["4"] = __torch__.torchvision.models.segmentation.deeplabv3.ASPPPooling
  def forward(self: __torch__.torch.nn.modules.container.ModuleList) -> None:
    _2 = uninitialized(None)
    ops.prim.RaiseException("")
    return _2
  def __len__(self: __torch__.torch.nn.modules.container.ModuleList) -> int:
    return 5
