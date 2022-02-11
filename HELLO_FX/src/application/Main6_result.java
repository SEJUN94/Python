package application;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class Main6_result extends Application {
	
	TextField tf;
	TextArea ta;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main6.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			tf = (TextField) scene.lookup("#tf");
			ta = (TextArea) scene.lookup("#ta");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myclick();
				}
			});
			

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	protected void myclick() {
		String dan = tf.getText();
		int idan = Integer.parseInt(dan);
		
		String text = "";
		
		text += dan + "X" + 1 +"="+(idan*1)+ "\n";
		text += dan + "X" + 2 +"="+(idan*2)+ "\n";
		text += dan + "X" + 3 +"="+(idan*3)+ "\n";
		text += dan + "X" + 4 +"="+(idan*4)+ "\n";
		text += dan + "X" + 5 +"="+(idan*5)+ "\n";

		text += dan + "X" + 6 +"="+(idan*6)+ "\n";
		text += dan + "X" + 7 +"="+(idan*7)+ "\n";
		text += dan + "X" + 8 +"="+(idan*8)+ "\n";
		text += dan + "X" + 9 +"="+(idan*9)+ "\n";
		
		ta.setText(text);
		
	}

	public static void main(String[] args) {
		launch(args);
	}
}
