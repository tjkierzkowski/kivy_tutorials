from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

class MyPaintWidget(Widget):
	def on_touch_down(self, touch):
		color = (random(),random(),random())
		with self.canvas:
			self.yellow_circle(touch, *color)

	def on_touch_move(self, touch):
		touch.ud['line'].points += [touch.x, touch.y]

	def yellow_circle(self, touch, *some_color):
			Color(*some_color)
			# Color(1,1,0)
			d = 30.
			Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d,d))
			touch.ud['line'] = Line(points=(touch.x,touch.y))

class MyPaintApp(App):
	def build(self):
		self.parent = Widget()
		self.painter = MyPaintWidget()
		self.clear_button = Button(text="Clear")
		self.parent.add_widget(self.painter)
		self.parent.add_widget(self.clear_button)
		self.clear_button.bind(on_release=self.clear_canvas_action)
		return self.parent

	def clear_canvas_action(self, obj):
		self.painter.canvas.clear()



if __name__ == "__main__":
	MyPaintApp().run()