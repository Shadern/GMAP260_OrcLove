import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import javax.imageio.ImageIO;
import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class OrcGame
{
	private JFrame frame;
	private JPanel panel;
	private static final String SCENEPATH = "scenes.txt";
	
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
		String image, text;
		
		public void display(JPanel panel)
		{
			System.out.println(getID() + " painting " + panel);
			try
			{
				panel.add(new JLabel(new ImageIcon(ImageIO.read(new File(image)))));
			}
			catch(Throwable e)
			{
				e.printStackTrace();
				System.exit(1);
			}
			frame.repaint();
		}
		
		public BasicScene load(BufferedReader reader)
		{
			//will use a loop to read variable amounts of data, for now just hard coded
			//for(String line = reader.readLine(); line != null && !line.equals(""); line = reader.readLine())
			
			try
			{
				id = reader.readLine();
				image = reader.readLine();
				text = reader.readLine();
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
		changeScene(scenes.get("a"));
	}
	
	private void changeScene(Scene s) //might preload images for the upcoming scenes
	{
		currentScene = s;
		frame.setContentPane(panel = new JPanel());
		panel.add(new JLabel("test"));
		s.display(panel);
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
						System.out.println("loaded scene " + s.getID());
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