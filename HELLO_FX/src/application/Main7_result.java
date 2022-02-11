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

public class Main7_result extends Application {
	
	TextField tf_mine; 
	TextField tf_com;
	TextField tf_result; 
	
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main7.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
 			
			tf_mine = (TextField) scene.lookup("#tf_mine");
			tf_com = (TextField) scene.lookup("#tf_com");
			tf_result = (TextField) scene.lookup("#tf_result");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				
				@Override
				public void handle(Event event) {
					myclick();
				}
			});
			tf_mine.setOnKeyPressed(new EventHandler<KeyEvent>() {

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
		mine = tf_mine.getText();
		
		double rnd = Math.random();
		if(rnd >0.66) {
			com = "가위";
		}else if(rnd > 0.33) {
			com = "바위";
		}else {
			com="보";
		}
		
		if(com.equals("가위") && mine.equals("가위")) result = "비김";
		if(com.equals("가위") && mine.equals("바위")) result = "이김";
		if(com.equals("가위") && mine.equals("보")) result = "짐";
		
		if(com.equals("바위") && mine.equals("가위")) result = "짐";
		if(com.equals("바위") && mine.equals("바위")) result = "비김";
		if(com.equals("바위") && mine.equals("보")) result = "이김";
		
		if(com.equals("보") && mine.equals("가위")) result = "이김";
		if(com.equals("보") && mine.equals("바위")) result = "짐";
		if(com.equals("보") && mine.equals("보")) result = "비김";
		
		tf_com.setText(com);
		tf_result.setText(result);
	}

	public static void main(String[] args) {
		launch(args);
	}
}
