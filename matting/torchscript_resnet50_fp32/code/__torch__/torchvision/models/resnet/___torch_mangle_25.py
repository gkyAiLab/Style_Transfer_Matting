class Bottleneck(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  stride : int
  conv1 : __torch__.torch.nn.modules.conv.___torch_mangle_19.Conv2d
  bn1 : __torch__.torch.nn.modules.batchnorm.___torch_mangle_3.BatchNorm2d
  conv2 : __torch__.torch.nn.modules.conv.___torch_mangle_20.Conv2d
  bn2 : __torch__.torch.nn.modules.batchnorm.___torch_mangle_3.BatchNorm2d
  conv3 : __torch__.torch.nn.modules.conv.___torch_mangle_21.Conv2d
  bn3 : __torch__.torch.nn.modules.batchnorm.___torch_mangle_22.BatchNorm2d
  relu : __torch__.torch.nn.modules.activation.ReLU
  downsample : __torch__.torch.nn.modules.container.___torch_mangle_24.Sequential
  def forward(self: __torch__.torchvision.models.resnet.___torch_mangle_25.Bottleneck,
    x: Tensor) -> Tensor:
    out = (self.conv1).forward(x, )
    out0 = (self.bn1).forward(out, )
    out1 = (self.relu).forward(out0, )
    out2 = (self.conv2).forward(out1, )
    out3 = (self.bn2).forward(out2, )
    out4 = (self.relu).forward(out3, )
    out5 = (self.conv3).forward(out4, )
    out6 = (self.bn3).forward(out5, )
    identity = (self.downsample).forward(x, )
    out7 = torch.add_(out6, identity, alpha=1)
    return (self.relu).forward(out7, )
