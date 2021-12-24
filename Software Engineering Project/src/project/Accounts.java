package project;

import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;


public class Accounts {

	// ********* //
	// VARIABLES //
	// ********* //
	private static double accountBalance = 0.0;
	private static double escoBalance = 0.0;
	private static double nytaxcollected = 0.0;
	private static double njtaxcollected = 0.0;
	private static double cttaxcollected = 0.0;

	//private static Object acct;

	//private static Object file;
	private static double expenses = 0.0;
	//private double amount;
	
	public Accounts()
	{
		super();
		accountBalance = setAccountBalance();
		escoBalance = setEscoBalance();
		expenses = setExpenses();
		
	  
            
		// ***************************************************************** //
		// 		   FORMAT FOR HOW THE DATE IS DISPLAY IN THE CSV FILE        //
		// STRING = (CLIENT NAME AND ID, STATE, DATE, INCOME, EXPENSES, TAX) //
		// ***************************************************************** //
		
		String fileName = "/Users/Starlyn/Documents/workspace/Software Engineering Project/data/food_truck.csv";
        Scanner inputStream = null;
        PrintWriter outputStream = null;// object to output to the file
		try {
			
			int numCounter = 0;
		
		    inputStream = new Scanner(new File(fileName));
		    inputStream.nextLine();
			while (inputStream.hasNextLine()) {
				String data = inputStream.next();
				String[] values = data.split(",");
				numCounter++;
				outputStream = new PrintWriter("Statement"+ numCounter +".txt");
				
				
				
				// ************************ //
				// ADD VALUES INTO ACCOUNTS //
				// ************************ //
				double bal = Double.parseDouble(values[3]);
				System.out.println("The income for the date" + values[2] + "is: " 
						+ bal);
				
				outputStream.println("The income for the date" + values[2] + "is: " 
						+ bal);
				
				accountBalance = accountBalance + bal;
				
				
				double escobal = Double.parseDouble(values[5]);
				escoBalance = escoBalance + escobal;
				
				System.out.println("The tax collected for the date" + values[2] + "is: " 
						+ escobal);
				
				outputStream.println("The tax collected for the date" + values[2] + "is: " 
						+ escobal);
				
				double expenses = Double.parseDouble(values[4]);
				accountBalance = accountBalance - expenses;
				
				
				System.out.println("The expenses for the date" + values[2] + "is: " 
						+ expenses);
				
				outputStream.println("The expenses for the date" + values[2] + "is: " 
						+ expenses);
				
				// ******************************************************************** //
				// DEPOSIT AMOUNTS INTO EACH ACCOUNT CHECKING AND ESCO PER EACH COMPANY //
				// ******************************************************************** //
				accountBalance = getAccountBalance(accountBalance);
				double newAccountBalance = depositInChecking(accountBalance, bal);
				
				System.out.println("The new account balance is: " + newAccountBalance);
				outputStream.println("The new account balance is: " + newAccountBalance);
				
				
				if ( values[1] == "NY")
				{
				       nytaxcollected = nytaxcollected + Double.parseDouble(values[5]);
				       
				       System.out.println("the amount of total ny tax collected is: " +
				       nytaxcollected);
				       
				       outputStream.println("the amount of total ny tax collected is: " +
						       nytaxcollected);
				}
				else if (values[1] == "NJ")
				{
					njtaxcollected = njtaxcollected + Double.parseDouble(values[5]);
					
					System.out.println("the amount of NJ tax collected is: "+ 
					njtaxcollected);
					
					outputStream.println("the amount of NJ tax collected is: "+ 
							njtaxcollected);
				}
				else if (values[1] == "CT")
				{
					cttaxcollected = cttaxcollected + Double.parseDouble(values[5]);
					
					System.out.println("the amount of CT tax collected is: " + 
					cttaxcollected);
					
					outputStream.println("the amount of CT tax collected is: " + 
							cttaxcollected);
				}
				escoBalance = getEscoBalance(escoBalance);
				double newEscoBalance = depositInEsco(escoBalance, escobal);
				
				System.out.println("The new Esco balance is: " + newEscoBalance);
				outputStream.println("The new Esco balance is: " + newEscoBalance);

			}
			inputStream.close();
            outputStream.close();
		} catch(FileNotFoundException e){
			e.printStackTrace();
		}
	   
	}
	
	

	// ************************* //
		// SETTER FOR ACCOUNTBALANCE //
		// ************************* // 
		public static double setAccountBalance(){ 
			double accountBalance = 0.0;
			return accountBalance;
		}

		// *********************** //
		// SETTER FOR ESCO BALANCE //
		// *********************** //
		public static double setEscoBalance(){
			double escoBalance = 0.0;
			return escoBalance;
		}

		// ******************************* //
		// SETTER AND GETTER FOR EXPENSIVE //
		// ******************************* //
		public static double setExpenses(){
			double expenses = 0.0;
			return expenses;
		}

		// ************************** //
		// GETTER FOR ACCOUNT BALANCE //
		// ************************* // 
		public static double getAccountBalance( double bal ) {
			accountBalance = bal;
			return accountBalance;
		}

		// ********************** //
		// GETTER FOR ESCOBALANCE //
		// ********************** //
		public static double getEscoBalance( double bal ){
			escoBalance = bal;
			return escoBalance;
		}

		// ******************* //
		// GETTER FOR EXPENSES //
		// ******************* //
		public static double getExpenses( double amount) {
			expenses = amount;
			return expenses;
		}

		// **************************** //
		// DISPLAY BALANCE TO TEXT AREA //
		// **************************** //
		public static double displayAccountBalance(double accountBalance){
			accountBalance = Accounts.accountBalance;
			return accountBalance;
		}

		// ******************** //
		// DISPLAY ESCO BALANCE //
		// ******************** //
		public static double displayEscoBalance(double escoBalance){
			escoBalance = Accounts.escoBalance;
			return escoBalance;
		}

		// ************************************************************ //
		// DEPOSITS INTO CHECKING ACCOUNT & RETURNS NEW ACCOUNT BALANCE //
		// ************************************************************ //
		public static double depositInChecking(double amount, double accountBalance){
			accountBalance = amount + accountBalance;
			return accountBalance;
		}

		// ************************************************************* //
		// DEPOSITS INTO TAX ACCOUNT RETURN NEW SALESTAX ACCOUNT BALANCE //
		// ************************************************************* //
		public static double depositInEsco(double amount, double escoBalance){
			escoBalance = amount + escoBalance;
			return escoBalance;
		}

	

		



	/*
	@SuppressWarnings("unused")
	private void csvLagguage_ComapanyReader(String fName) { 
		File file = new File(fName);

		try {
			Scanner inputStream = new Scanner(file);
			// inputStream.next();
			while (inputStream.hasNext()) {
				String data = inputStream.nextLine();
				String[] values = data.split(",");
				System.out.println(data);
				System.out.println(values[3]);
				//sales.add(values[0]);
				//salestax.add(values[1]);
				//add(values[2]);
				//year.add(values[3]);
				//saleValue.add(values[4]);
			}
			inputStream.close();

		} catch(FileNotFoundException e){
			e.printStackTrace();
		}
	}

	@SuppressWarnings("unused")
	private void csvBreadFactoryReader(String fName) { 
		File file = new File(fName);

		try {
			Scanner inputStream = new Scanner(file);
			// inputStream.next();
			while (inputStream.hasNext()) {
				String data = inputStream.nextLine();
				String[] values = data.split(",");
				System.out.println(data);
				System.out.println(values[3]);
				//sales.add(values[0]);
				//salestax.add(values[1]);
				//add(values[2]);
				//year.add(values[3]);
				//saleValue.add(values[4]);
			}
			inputStream.close();

		} catch(FileNotFoundException e){
			e.printStackTrace();
		}
	}

	@SuppressWarnings("unused")
	private void csvBatteryCompanyReader(String fName) {
		File file = new File(fName);

		try {
			Scanner inputStream = new Scanner(file);
			// inputStream.next();
			while (inputStream.hasNext()) {
				String data = inputStream.nextLine();
				String[] values = data.split(",");
				System.out.println(data);
				System.out.println(values[3]);
				//sales.add(values[0]);
				//salestax.add(values[1]);
				//add(values[2]);
				//year.add(values[3]);
				//saleValue.add(values[4]);
			}
			inputStream.close();

		} catch(FileNotFoundException e){
			e.printStackTrace();
		}
	}

	@SuppressWarnings("unused")
	private void csvSandwich_ShopReader(String fName) {
		File file = new File(fName);

		try {
			Scanner inputStream = new Scanner(file);
			// inputStream.next();
			while (inputStream.hasNext()) {
				String data = inputStream.nextLine();
				String[] values = data.split(",");
				System.out.println(data);
				System.out.println(values[3]);
				//sales.add(values[0]);
				//salestax.add(values[1]);
				//add(values[2]);
				//year.add(values[3]);
				//saleValue.add(values[4]);
			}
			inputStream.close();

		} catch(FileNotFoundException e){
			e.printStackTrace();
		}
	}
*/
	
	

	/*
	// ********************************************** //
	// METHOD FOR PRINTING TO A TEXT FILE OR PDF FILE //
	// ********************************************** //
	public File printDocument(File fname){
		this.fname = fname;
		String date = values[2];
		int sNumber = 0;
		File doc = new File("Statement for"+ sNumber+ date+".docx");
		try {
			Scanner outputStream = new Scanner(doc);
            for( int line = 0; line <= fname.length(); line++) {
            	//outputStream = [line].write();
            }
		}catch( Exception e) {
			e.printStackTrace();
		}
		return doc;
	}
	 */

	

	
	// **************************** //
	// METHOD FOR PRINTING PDF FILE //
	// **************************** //
	/*
	public void writeStatement(){
		@SuppressWarnings("resource")
		Scanner input = new Scanner(System.in);
		// LOOP UNTIL END OF THE FILE //
		while( input.hasNext()){
			try{
				//System.out.println(data);
				//System.out.println(values[3]);
				//sales.add(values[0]);
				//salestax.add(values[1]);
				//.add(values[2]);
				//year.add(values[3]);
				//saleValue.add(values[4]);
				//get( input.nextInt(values[3]));
			}
			catch(Exception e){
				e.printStackTrace();
			}
	*/

	// *********** //
	// MAIN METHOD //
	// *********** //
	public static void main(String[] args) {
            
              new Accounts();		
	}

	
}