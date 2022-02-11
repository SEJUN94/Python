package application;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.TreeSet;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class Main5 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main5.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			
			Label lbl01 = (Label) scene.lookup("#lbl01");
			Label lbl02 = (Label) scene.lookup("#lbl02");
			Label lbl03 = (Label) scene.lookup("#lbl03");
			Label lbl04 = (Label) scene.lookup("#lbl04");
			Label lbl05 = (Label) scene.lookup("#lbl05");
			Label lbl06 = (Label) scene.lookup("#lbl06");
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					HashSet<Integer> num = new HashSet<Integer>();
					
					for(int i= 1;num.size()<6;i++) {
						if(num.size()<6) {
						int lotto = (int)(Math.random()*45)+1;
						num.add(lotto);
						System.out.println(num);
						}
					}
					
					List<Integer> list = new ArrayList<Integer>();
					list.addAll(num);
					
					Collections.sort(list);
				
					System.out.println(list);
					System.out.println(list.get(0));
					System.out.println(list.get(1));
					System.out.println(list.get(2));
					
					
					lbl01.setText(list.get(0)+"");
					lbl02.setText(list.get(1)+"");
					lbl03.setText(list.get(2)+"");
					lbl04.setText(list.get(3)+"");
					lbl05.setText(list.get(4)+"");
					lbl06.setText(list.get(5)+"");
					
					lbl01.getText();
					lbl02.getText();
					lbl03.getText();
					lbl04.getText();
					lbl05.getText();
					lbl06.getText();
					
					
					
				}
			});
			

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		launch(args);
	}
}
