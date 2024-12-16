from manim import *

class Fillers(Scene):
    def construct(self):
        # Set up initial title
        title = Text("How DeFi Fillers Work", font_size=40)
        self.play(Write(title))
        self.wait()
        self.play(title.animate.to_edge(UP))

        # Create swap pool representation
        pool = Circle(radius=1.5, color=BLUE)
        pool_label = Text("Liquidity\nSource", font_size=24).move_to(pool)
        pool_group = VGroup(pool, pool_label).move_to(ORIGIN)

        # Create user order representation
        user = Circle(radius=0.3, color=GREEN).move_to(LEFT * 4)
        user_label = Text("User", font_size=24).next_to(user, DOWN)
        user_group = VGroup(user, user_label)

        # Create filler representation
        filler = Circle(radius=0.3, color=YELLOW).move_to(RIGHT * 4)
        filler_label = Text("Filler", font_size=24).next_to(filler, DOWN)
        filler_group = VGroup(filler, filler_label)

        # Show initial setup
        self.play(
            Create(pool_group),
            Create(user_group),
            Create(filler_group)
        )
        self.wait()

        # Step 1: User submits order
        order = Rectangle(height=0.5, width=1, color=GREEN)
        order_label = Text("Order", font_size=20).move_to(order)
        order_group = VGroup(order, order_label).next_to(user, RIGHT)
        
        self.play(Create(order_group))
        self.play(
            order_group.animate.move_to(ORIGIN + UP * 2),
            Flash(order_group)
        )
        
        # Add explanation text
        step1_text = Text("1. User submits trade order via signing an on chain message", font_size=24).to_edge(DOWN)
        self.play(Write(step1_text))
        self.wait()

        # Step 2: Filler analyzes opportunity
        scanning_arrow = Arrow(filler.get_center(), order_group.get_center(), color=YELLOW)
        self.play(Create(scanning_arrow))
        
        self.play(FadeOut(step1_text))
        step2_text = Text("2. Filler analyzes profitability", font_size=24).to_edge(DOWN)
        self.play(Write(step2_text))
        self.wait()

        # Step 3: Filler executes trade
        trade_path = [
            order_group.get_center(),
            pool_group.get_center(),
            filler.get_center()
        ]
        trade_line = VMobject()
        trade_line.set_points_smoothly(trade_path)
        
        self.play(FadeOut(scanning_arrow))
        self.play(FadeOut(step2_text))
        step3_text = Text("3. Filler executes profitable trade", font_size=24).to_edge(DOWN)
        self.play(Write(step3_text))
        
        dot = Dot(color=YELLOW)
        self.play(
            MoveAlongPath(dot, trade_line),
            rate_func=linear
        )
        self.wait()

        # Step 4: Show profit distribution
        profit_box = Rectangle(height=0.8, width=1.2, color=GREEN_A)
        profit_text = Text("Profit", font_size=20).move_to(profit_box)
        profit_group = VGroup(profit_box, profit_text).next_to(filler, UP)
        
        self.play(FadeOut(step3_text))
        step4_text = Text("4. Filler keeps profit margin", font_size=24).to_edge(DOWN)
        self.play(Write(step4_text))
        
        self.play(
            Create(profit_group),
            Flash(profit_group)
        )
        self.wait()

        # Final message
        final_text = Text("Fillers help maintain market efficiency", font_size=32).to_edge(DOWN)
        self.play(
            FadeOut(step4_text),
            Write(final_text)
        )
        self.wait(2)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )