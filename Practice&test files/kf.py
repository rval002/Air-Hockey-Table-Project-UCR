import numpy as np

class KF:
    def __init__(self,initx: float,
                      initv: float,
                      accel_variance: float) -> None:
        #mean of state
        self._x = np.array([initx, initv])
        self._accel_variance = accle_variance

        # covariance of state
        self.P = np.eye(2)

        def predict(self, dt: float) -> None:
            # x = F  x
            # P = F  P  Ft + G Gt a
            pass

        @property
        def pos(self) -> float:
            return self._x[0]

        @property
        def vel(self) -> float:
            return self._x[1]
