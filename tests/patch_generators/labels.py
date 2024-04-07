#!/usr/bin/env python3
import metapatch


class TestMetaPatch(metapatch.PatchGenerator):
    """Test metapatch."""

    title = "Test"
    description = "A test patch."

    def generate(self) -> None:
        """Generate patch."""
        self.add_controller("P2B8", 1)
        self.add_controller("P2B8", 2)
        self.add_controller("P2B8", 3)
        self.add_controller("E4", 4)
        self.add_label("I1", "Input 1", "This is input 1")
        self.add_label("O1", "Output 1")
        self.add_label("G2.7", "Gate 7", "Gate jack number 7")
        self.add_label("E4.3", "Encoder", "Encoder 3 on module 4")
