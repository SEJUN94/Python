package application;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class Main4_result extends Application {
	
	TextField tfMine; 
	TextField tfCom;
	TextField tfResult; 
	
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main4.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
 			
			tfMine = (TextField) scene.lookup("#tfMine");
			tfCom = (TextField) scene.lookup("#tfCom");
			tfResult = (TextField) scene.lookup("#tfResult");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				
				@Override
				public void handle(Event event) {
					myclick();
				}
			});
			tfMine.setOnKeyPressed(new EventHandler<KeyEvent>() {

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
		String com = "";
		String mine = "";
		String result = "";
		mine = tfMine.getText();
		
		double rnd = Math.random();
		if(rnd>0.5) {
			com = "홀";
		}else {
			com = "짝";
		}
		if(com.equals(mine)) {
			result = "이김";
		}else {
			result = "짐";
		}
		tfCom.setText(com);
		tfResult.setText(result);
	}

	public static void main(String[] args) {
		launch(args);
	}
}
