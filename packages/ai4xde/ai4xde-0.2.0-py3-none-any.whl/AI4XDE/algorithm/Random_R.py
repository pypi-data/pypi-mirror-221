import deepxde as dde
from ..cases.PDECases import Diffusion
from ..solver.PDESolver import PINNSolver


class Random_R(PINNSolver):
    def __init__(self, PDECase, P):
        super().__init__(name=f"Random_R_P_{P}", PDECase=PDECase)
        self.P = P
        self.resampler = dde.callbacks.PDEPointResampler(period=self.P)

    def closure(self):
        self.train_step(callbacks=[self.resampler])


if __name__ == "__main__":
    PDECase = Diffusion(NumDomain=2000)
    solver = Random_R(P=00, PDECase=PDECase)
    solver.train()
    solver.save(add_time=True)
