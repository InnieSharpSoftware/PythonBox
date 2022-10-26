import System.Drawing
import System.Windows.Forms
import System
import System.IO

from System.Drawing import *
from System.Windows.Forms import *
from System import *
from System.IO import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._richTextBox1 = System.Windows.Forms.RichTextBox()
		self._saveToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._openToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._saveFileDialog1 = System.Windows.Forms.SaveFileDialog()
		self._openFileDialog1 = System.Windows.Forms.OpenFileDialog()
		self._menuStrip1.SuspendLayout()
		self.SuspendLayout()
		# 
		# menuStrip1
		# 
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._saveToolStripMenuItem,
			self._openToolStripMenuItem]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(613, 24)
		self._menuStrip1.TabIndex = 0
		self._menuStrip1.Text = "menuStrip1"
		# 
		# richTextBox1
		# 
		self._richTextBox1.Dock = System.Windows.Forms.DockStyle.Fill
		self._richTextBox1.Location = System.Drawing.Point(0, 24)
		self._richTextBox1.Name = "richTextBox1"
		self._richTextBox1.Size = System.Drawing.Size(613, 293)
		self._richTextBox1.TabIndex = 1
		self._richTextBox1.Text = ""
		self._richTextBox1.WordWrap = False
		# 
		# saveToolStripMenuItem
		# 
		self._saveToolStripMenuItem.Name = "saveToolStripMenuItem"
		self._saveToolStripMenuItem.Size = System.Drawing.Size(43, 20)
		self._saveToolStripMenuItem.Text = "Save"
		self._saveToolStripMenuItem.Click += self.SaveToolStripMenuItemClick
		# 
		# openToolStripMenuItem
		# 
		self._openToolStripMenuItem.Name = "openToolStripMenuItem"
		self._openToolStripMenuItem.Size = System.Drawing.Size(48, 20)
		self._openToolStripMenuItem.Text = "Open"
		self._openToolStripMenuItem.Click += self.OpenToolStripMenuItemClick
		# 
		# saveFileDialog1
		# 
		self._saveFileDialog1.FileOk += self.SaveFileDialog1FileOk
		# 
		# openFileDialog1
		# 
		self._openFileDialog1.FileOk += self.OpenFileDialog1FileOk
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(613, 317)
		self.Controls.Add(self._richTextBox1)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "MainForm"
		self.Text = "PythonBox"
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()


	def SaveToolStripMenuItemClick(self, sender, e):
		self._saveFileDialog1.ShowDialog()

	def SaveFileDialog1FileOk(self, sender, e):
		File.WriteAllLines(self._saveFileDialog1.FileName, self._richTextBox1.Lines)

	def OpenToolStripMenuItemClick(self, sender, e):
		self._openFileDialog1.ShowDialog()

	def OpenFileDialog1FileOk(self, sender, e):
		self._richTextBox1.Lines = File.ReadAllLines(self._openFileDialog1.FileName)