class ASPPConv(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  __annotations__["0"] = __torch__.torch.nn.modules.conv.___torch_mangle_47.Conv2d
  __annotations__["1"] = __torch__.torch.nn.modules.batchnorm.___torch_mangle_3.BatchNorm2d
  __annotations__["2"] = __torch__.torch.nn.modules.activation.___torch_mangle_42.ReLU
  def forward(self: __torch__.torchvision.models.segmentation.deeplabv3.___torch_mangle_48.ASPPConv,
    input: Tensor) -> Tensor:
    _0 = getattr(self, "0")
    _1 = getattr(self, "1")
    _2 = getattr(self, "2")
    input0 = (_0).forward(input, )
    input1 = (_1).forward(input0, )
    return (_2).forward(input1, )
  def __len__(self: __torch__.torchvision.models.segmentation.deeplabv3.___torch_mangle_48.ASPPConv) -> int:
    return 3
