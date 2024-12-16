from manim import *

class AMMTokenSwap(Scene):
    def construct(self):
        # Configuration
        initial_eth = 100
        initial_usdc = 200000
        swap_amount = 50
        k = initial_eth * initial_usdc

        # Create simpler title using Text instead of Tex
        title = Text("ETH-USDC Pool: Token Swap Impact", font_size=36)
        title.to_edge(UP)
        
        # Create axes with minimal text
        axes = Axes(
            x_range=[0, 200, 50],
            y_range=[0, 400000, 100000],
            x_length=6,
            y_length=5,
            tips=False,
            axis_config={
                "include_numbers": False,
                "include_ticks": True
            }
        ).shift(DOWN * 0.5)

        # Add labels using Text
        x_label = Text("ETH", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("USDC", font_size=24).next_to(axes.y_axis, UP)
        
        # Create the curve
        curve = axes.plot(
            lambda x: k/x if x > 0 else 0,
            x_range=[k/400000, 200],
            color=BLUE,
        )

        # Add points
        initial_dot = Dot(axes.c2p(initial_eth, initial_usdc), color=GREEN)
        final_eth = initial_eth + swap_amount
        final_usdc = k / final_eth
        final_dot = Dot(axes.c2p(final_eth, final_usdc), color=RED)

        # Add simple labels using Text
        initial_label = Text("Start", font_size=16).next_to(initial_dot, RIGHT)
        final_label = Text("End", font_size=16).next_to(final_dot, RIGHT)

        # Animation sequence
        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(curve))
        self.play(Create(initial_dot), Write(initial_label))
        
        # Animate the swap
        arrow = Arrow(
            start=axes.c2p(initial_eth, initial_usdc),
            end=axes.c2p(final_eth, final_usdc),
            color=YELLOW,
        )
        self.play(Create(arrow))
        self.play(Create(final_dot), Write(final_label))
        
        # Add impact text
        impact_text = Text("Large swaps = Big price impact!", 
                         color=RED, 
                         font_size=24).to_edge(DOWN)
        self.play(Write(impact_text))
        
        self.wait(2)
        
# manim -pql amm.py AMMTokenSwap