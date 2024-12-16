from manim import *

class SandwichAttack(Scene):
    def construct(self):
        # Title and Introduction
        title = Text("Sandwich Attack in Ethereum", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Create participants
        attacker = Circle(color=RED, fill_opacity=0.5).scale(0.7)
        user = Circle(color=BLUE, fill_opacity=0.5).scale(0.7)
        dex = Rectangle(color=GREEN, fill_opacity=0.5, height=1, width=2)

        # Label participants
        attacker_label = Text("MEV Attacker", font_size=20).next_to(attacker, DOWN)
        user_label = Text("User", font_size=20).next_to(user, DOWN)
        dex_label = Text("DEX", font_size=20).next_to(dex, DOWN)

        # Position participants
        attacker.move_to(LEFT * 4)
        user.move_to(ORIGIN)
        dex.move_to(RIGHT * 4)

        # Add participants to scene
        self.play(
            Create(attacker), Create(user), Create(dex),
            Write(attacker_label), Write(user_label), Write(dex_label)
        )
        self.wait(1)

        # User Transaction Visualization
        user_tx = Text("Large Token Swap", font_size=24, color=BLUE)
        user_tx.next_to(user, UP)
        self.play(Write(user_tx))
        self.wait(1)

        # First Attack Transaction (Front-running)
        front_run_tx = Arrow(attacker.get_right(), user.get_left(), color=RED)
        front_run_label = Text("Front-run\nBuy Tokens", font_size=20, color=RED)
        front_run_label.next_to(front_run_tx, UP)
        self.play(
            Create(front_run_tx),
            Write(front_run_label)
        )
        self.wait(1)

        # User's Original Transaction
        user_swap_tx = Arrow(user.get_right(), dex.get_left(), color=BLUE)
        user_swap_label = Text("Original\nSwap", font_size=20, color=BLUE)
        user_swap_label.next_to(user_swap_tx, UP)
        self.play(
            Create(user_swap_tx),
            Write(user_swap_label)
        )
        self.wait(1)

        # Back-running Transaction
        back_run_tx = Arrow(dex.get_right(), attacker.get_left(), color=RED)
        back_run_label = Text("Back-run\nSell Tokens", font_size=20, color=RED)
        back_run_label.next_to(back_run_tx, DOWN)
        self.play(
            Create(back_run_tx),
            Write(back_run_label)
        )
        self.wait(2)

        # Profit Calculation
        profit_text = Text("Attacker Profit:", font_size=30)
        profit_value = Text("Price Impact Exploitation", font_size=24, color=GREEN)
        profit_group = VGroup(profit_text, profit_value).arrange(DOWN).to_edge(DOWN)
        
        self.play(
            Write(profit_text),
            Write(profit_value)
        )
        self.wait(3)

# To render: manim -pql sandwich.py SandwichAttack