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

public class Main5_result extends Application {

	Label lbl01;
	Label lbl02;
	Label lbl03;
	Label lbl04;
	Label lbl05;
	Label lbl06;

	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane) FXMLLoader.load(getClass().getResource("Main5.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();

			lbl01 = (Label) scene.lookup("#lbl01");
			lbl02 = (Label) scene.lookup("#lbl02");
			lbl03 = (Label) scene.lookup("#lbl03");
			lbl04 = (Label) scene.lookup("#lbl04");
			lbl05 = (Label) scene.lookup("#lbl05");
			lbl06 = (Label) scene.lookup("#lbl06");

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

	public void myclick() {
		int[] arr = {
			1,2,3,4,5,		6,7,8,9,10,
			11,12,13,14,15,	16,17,18,19,20,
			21,22,23,24,25,	26,27,28,29,30,
			31,32,33,34,35,	36,37,38,39,40,
			41,42,43,44,45
			};
		ArrayList<Integer> arr6 = new ArrayList<Integer>();
		
		while(arr6.size() < 6) {
			int rnd = (int)(Math.random()*45);
			
			if(arr[rnd]>0) {
				arr6.add(arr[rnd]);
				arr[rnd]=-1;
			}
			
			if(arr[rnd]>0) {
				arr6.add(arr[rnd]);
				arr[rnd]=-1;
			}
		}
		lbl01.setText(arr6.get(0)+"");
		lbl02.setText(arr6.get(1)+"");
		lbl03.setText(arr6.get(2)+"");
		lbl04.setText(arr6.get(3)+"");
		lbl05.setText(arr6.get(4)+"");
		lbl06.setText(arr6.get(5)+"");
		
	}

	
	public static void main(String[] args) {
		launch(args);
	}
}
