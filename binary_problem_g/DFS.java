import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class DFS {
	int max_rows;
	int max_cols;
	int[][] grid;
	int x1, y1, x2, y2;
	public static HashMap<String, Integer> already_visited = new HashMap<String, Integer>();
	public static ArrayList<String> stack = new ArrayList<String>();

	public DFS(int max_rows, int max_cols, int[][] grid, int x1, int y1, int x2, int y2) {
		this.max_rows = max_rows;
		this.max_cols = max_cols;
		this.grid = grid;
		this.x1 = x1;
		this.y1 = y1;
		this.x2 = x2;
		this.y2 = y2;
	}

	int getValueInCell(int row, int col) {
		return this.grid[row][col];
	}


	boolean checkVisited(int row, int col, int val, String cell, HashMap<String, Integer> already_visited) {
		if (row > this.max_rows || row < 0 || col > this.max_cols || col < 0) return true;
		int new_val = this.getValueInCell(row, col);
		if (new_val != val) return true;
		
		String new_cell = Integer.toString(row);
		new_cell += "@" + Integer.toString(col);
		if (already_visited.containsKey(new_cell)) {
			return true;
		} else {
			already_visited.put(new_cell, new_val);
			stack.add(new_cell);
			return false;
		}
	}


	int dfs() {
		String final_dest = Integer.toString(this.x2);
		//final_dest += Integer.toString(this.y2);
		final_dest += "@" + Integer.toString(this.y2);

		int start_val = this.getValueInCell(x1, y1);
		int end_val = this.getValueInCell(x2, y2);
		if (start_val != end_val) return -1;

		String key = Integer.toString(this.x1);
		//key += Integer.toString(this.y1);
		key += "@" + Integer.toString(this.y1);
		stack.add(key);

		int current_row;
		int current_col;
		String current_cell;
		int current_val;
		boolean visited;
		String[] splitted;
		while (!stack.isEmpty()) {
			current_cell = stack.get(stack.size() - 1);
			stack.remove(stack.size() - 1);
			
			splitted = current_cell.split("@", 2);
			//current_row = Character.getNumericValue(current_cell.charAt(0));
			current_row = Integer.parseInt(splitted[0]);
			current_col = Integer.parseInt(splitted[1]);
			//current_col = Character.getNumericValue(current_cell.charAt(1));
			current_val = this.getValueInCell(current_row, current_col);

			already_visited.put(current_cell, current_val);

			if (current_cell.equals(final_dest)) return current_val;

			visited = this.checkVisited(current_row, current_col+1, current_val, current_cell, already_visited);
			visited = this.checkVisited(current_row, current_col-1, current_val, current_cell, already_visited);
			visited = this.checkVisited(current_row+1, current_col, current_val, current_cell, already_visited);
			visited = this.checkVisited(current_row-1, current_col, current_val, current_cell, already_visited);
		}
		return -1;
	}


	String runDFS() {
		stack = new ArrayList<String>();
		already_visited = new HashMap<String, Integer>();
		int result = dfs();
		if (result == 1) return "decimal";
		else if (result == 0) return "binary";
		else return "neither";
	}


	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//Scanner sc = new Scanner(System.in);
		try {
			String line = br.readLine();
			String[] parsed_line = line.trim().split("\\s+");
			int grid_row = Integer.parseInt(parsed_line[0]);
			int grid_col = Integer.parseInt(parsed_line[1]);
			int[][] grid = new int[grid_row][grid_col];

			char c;
			int element;
			for (int i = 0; i < grid_row; i++) {
				line = br.readLine();
				for (int j = 0; j < grid_col; j++) {
					c = line.charAt(j);
					element = Character.getNumericValue(c);
					grid[i][j] = element;
				}
			}

			DFS dfs;

			line = br.readLine();
			parsed_line = line.trim().split("\\s+");
			int num_queries = Integer.parseInt(parsed_line[0]);
			int x1, y1, x2, y2;
			String out;
			for (int i = 0; i < num_queries; i++) {
				line = br.readLine();
				parsed_line = line.trim().split("\\s+");
				x1 = Integer.parseInt(parsed_line[0]);
				y1 = Integer.parseInt(parsed_line[1]);
				x2 = Integer.parseInt(parsed_line[2]);
				y2 = Integer.parseInt(parsed_line[3]);
				dfs = new DFS(grid_row-1, grid_col-1, grid, x1-1, y1-1, x2-1, y2-1);
				out = dfs.runDFS();
				System.out.println(out);
			}
		} catch(Exception e) {
			System.out.print(e);
		}
	}

}