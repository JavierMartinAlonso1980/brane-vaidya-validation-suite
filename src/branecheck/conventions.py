from dataclasses import dataclass

@dataclass(frozen=True)
class Convention:
    signature: str = "-++++"
    epsilon: int = -1              # ds²=-f du²+2 epsilon du dr+...
    normal_orientation: str = "decreasing-r"
    z2_symmetric: bool = True
    q_positive_means: str = "injection-into-brane"

    def __post_init__(self):
        if self.epsilon not in (-1, 1):
            raise ValueError("epsilon must be ±1")
