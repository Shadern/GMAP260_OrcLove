import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.imageio.ImageIO;
import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class OrcGame
{
	private JFrame frame;
	private JPanel panel;
	private static final String SCENEPATH = "scenes.txt";
	private static final Dimension PANELSIZE = new Dimension(800, 600);
	
	private Scene currentScene;
	
	Map<String, Scene> scenes;
	
	public static void main(String[] args)
	{
		new OrcGame().start();
	}
	
	private OrcGame()
	{
		scenes = loadScenes();
		
		frame = new JFrame();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setTitle("OrcGame");
		frame.setContentPane(panel = new JPanel());
		frame.setVisible(true);
		frame.setSize(800 + frame.getInsets().left - 1, 600 + frame.getInsets().top - 1);
		frame.setLocationRelativeTo(null);
		frame.setResizable(false);
	}
	
	private abstract class Scene
	{
		protected String id;
		
		public String getID()
		{
			return id;
		}
		
		public abstract void display(JPanel panel);
		
		public abstract Scene load(BufferedReader reader);
	}
	
	private class BasicScene extends Scene
	{
		public final Dimension IMAGESIZE = new Dimension(800, 400);
		public final Dimension TEXTSIZE = new Dimension(800, 50);
		public final Dimension BUTTONSIZE = new Dimension(800, 50);
		public final Color BACKGROUND = new Color(127, 127, 127); //new Color(34, 177, 76);
		public String image, text;
		public String[] targets, options;
		
		public void display(JPanel panel)
		{
			try
			{
				panel.setBackground(BACKGROUND);
				
				JLabel imageLabel = new JLabel(new ImageIcon(ImageIO.read(new File(image))));
				imageLabel.setSize(IMAGESIZE);
				imageLabel.setLocation(0, 0);
				panel.add(imageLabel);
				
				JLabel textLabel = new JLabel(text);
				textLabel.setSize(TEXTSIZE);
				textLabel.setLocation(0, 400);
				panel.add(textLabel);
				
				JButton[] buttons = new JButton[targets.length];
				for(int i = 0; i < buttons.length; i++)
				{
					buttons[i] = new JButton(options[i]);
					buttons[i].setSize(BUTTONSIZE);
					buttons[i].setLocation(0, 450 + i * 50);
					buttons[i].setActionCommand(targets[i]);
					buttons[i].addActionListener(new ActionListener()
					{
						public void actionPerformed(ActionEvent e)
						{
							changeScene(scenes.get(e.getActionCommand()));
						}
					});
					panel.add(buttons[i]);
					
					panel.setVisible(true);
				}
			}
			catch(Throwable e)
			{
				e.printStackTrace();
				System.exit(1);
			}
			//frame.repaint();
		}
		
		public BasicScene load(BufferedReader reader)
		{
			try
			{
				id = reader.readLine();
				image = reader.readLine();
				text = reader.readLine();
				
				List<String> lines = new ArrayList<String>();
				for(String line = reader.readLine(); line != null && !line.equals(""); line = reader.readLine())
					lines.add(line);
				
				targets = new String[lines.size()];
				options = new String[lines.size()];
				
				for(int i = 0; i < lines.size(); i++)
				{
					//split on first :
					int split = lines.get(i).indexOf(":");
					targets[i] = lines.get(i).substring(0, split);
					options[i] = lines.get(i).substring(split + 1);
				}
			}
			catch(IOException e)
			{
				e.printStackTrace();
				System.exit(1);
			}
			
			return this;
		}
	}
	
	private void start()
	{
		changeScene(scenes.get("mainmenu"));
	}
	
	private void changeScene(Scene s) //might preload images for the upcoming scenes
	{
		if(s == null)
			s = scenes.get("null");
		currentScene = s;
		frame.setContentPane(panel = new JPanel());
		panel.setSize(PANELSIZE);
		s.display(panel);
		//frame.pack(); //only use this if using a layout manager, otherwise it'll move things where you don't want them
		frame.repaint();
	}
	
	private Map<String, Scene> loadScenes()
	{
		try
		{
			Map<String, Scene> map = new HashMap<String, Scene>();
			BufferedReader reader = new BufferedReader(new FileReader(SCENEPATH));
			
			Scene s = null;
			for(String line = reader.readLine(); line != null; line = reader.readLine())
				switch(line)
				{
					case "basic":
						s = new BasicScene().load(reader);
						map.put(s.getID(), s);
						break;
				}
			
			reader.close();
			return map;
		}
		catch(IOException e)
		{
			e.printStackTrace();
			System.exit(1);
		}
		return null;
	}
}