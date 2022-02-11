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

public class Main7 extends Application {
	
	TextField tfMine; 
	TextField tfCom;
	TextField tfResult; 
	
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main7.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
 			
			tfMine = (TextField) scene.lookup("#tf_mine");
			tfCom = (TextField) scene.lookup("#tf_com");
			tfResult = (TextField) scene.lookup("#tf_result");
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
		if(rnd > 0 && rnd <= 0.33) {
			com = "가위";
		}else if(rnd > 0.33 && rnd <= 0.66) {
			com = "바위";
		}else if(rnd > 0.66 && rnd <= 1) {
			com="보";
		}
		
		if(com.equals(mine)) {
			result = "비김";
		}else if((mine.equals("가위") && com.equals("보")) ||
				 (mine.equals("바위") && com.equals("가위"))||
				 (mine.equals("보")  && com.equals("바위"))) {
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
