package application;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class Main8 extends Application {
	
	TextField tfFirst; 
	TextField tfLast;
	TextArea ta; 
	
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main8.fxml"));
			Scene scene = new Scene(root, 300, 300);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
 			
			tfFirst = (TextField) scene.lookup("#tfFirst");
			tfLast = (TextField) scene.lookup("#tfLast");
			ta = (TextArea) scene.lookup("#ta");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				
				@Override
				public void handle(Event event) {
					myclick();
				}
			});
			tfFirst.setOnKeyPressed(new EventHandler<KeyEvent>() {

				@Override
				public void handle(KeyEvent event) {
					System.out.println(event.getCode());
					if(event.getCode().equals(KeyCode.ENTER)) {
						myclick();
					}
					
				}

			});

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public void myclick() {
		String first = tfFirst.getText();
		String last = tfLast.getText();
		String result = "*";
		int ifirst = Integer.parseInt(first);
		int ilast = Integer.parseInt(last);
		
		for(;ifirst<ilast; ifirst++) {
			for(int i = 0; i<ifirst; i++) {
				System.out.print(result);
				result += "*";
			}
			System.out.println();
		}
		ta.setText(result);
		
	}

	public static void main(String[] args) {
		launch(args);
	}
}
