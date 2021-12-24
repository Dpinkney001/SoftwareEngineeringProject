/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author DUVALL NOTEBOOK
 * Duvall.Pinkney@gmail.com
 */

package project2018;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Battery_Company_Account {

	// ********* //
	// VARIABLES //
	// ********* //
	private static double accountBalance = 0.0;
	private static double escoBalance = 0.0;
	

	//private static Object acct;

	//private static Object file;
	public static double expenses = 0.0;
	public static double remainingBalance = 0.0;
	public static double newTotalnytaxcollected;
	public static double newTotalcttaxcollected;
	//private double amount;
	public static double newTotalnjtaxcollected;
	public static double newTotalBostonTaxCollected;
	public static double newTotalChicagoTaxCollected;
	
	
	// *********** //
		// MAIN METHOD //
		// *********** //
		public static void main(String[] args) {
	           
		accountBalance = setAccountBalance();
		escoBalance = setEscoBalance();
		expenses = setExpenses();
	    
		double nytaxcollected = 0.0;
		double njtaxcollected = 0.0;
		double cttaxcollected = 0.0;
		double chicagoTaxCollected = 0.0;
		double bostonTaxCollected = 0.0;
            
		// ***************************************************************** //
		// 		   FORMAT FOR HOW THE DATE IS DISPLAY IN THE CSV FILE        //
		// STRING = (CLIENT NAME AND ID, STATE, DATE, INCOME, EXPENSES, TAX) //
		// ***************************************************************** //
		//change source file per program
		String fileName = "/Users/DUVALL NOTEBOOK/workspace/project 2018 version 8/src/data/battery_company.csv";
        Scanner inputStream = null;
        PrintWriter outputStream = null;// object to output to the html file
        //PrintWriter outputStream2 = null;// output to 
		try {
			
			int numCounter = 0;
			
			
		    inputStream = new Scanner(new File(fileName));
		    inputStream.nextLine();
			while (inputStream.hasNextLine()) {
				String data = inputStream.nextLine();
				String[] values = data.split(",");
				String batteryTransNum = values[0];
				String state = values[1];
				String date = values[2];
				String income = values[3];
				String expense = values[4];
				String tax = values[5];
				
				System.out.println(batteryTransNum);
				System.out.println(state);
				System.out.println(date);
				System.out.println(income);
				System.out.println(expense);
				System.out.println(tax);
				numCounter++;
				
				//change directory  per program
				outputStream = new PrintWriter("/Users/DUVALL NOTEBOOK/workspace/project 2018 version 8/src/public_html_Battery_Company/BatteryCompanyStatement"+ numCounter +".html");
				
				outputStream.println("<!DOCTYPE html>");
				outputStream.println("<html>");
				outputStream.println("        <head>");
				outputStream.println("                <title>Battery Company Statement"+ numCounter +"</title>");
				outputStream.println("<meta charset='UTF-8'>");
				outputStream.println("<meta name='viewport' content='width=device-width, initial-scale=1'>");
				outputStream.println(" <link rel='stylesheet' href='website.css'>");
				outputStream.println("        </head>");
				outputStream.println("<body>");
			    outputStream.println("<p>");
				outputStream.println("<nav> <a href='mainpage.html'>Main page</a> <a href='battery_company Home.html'>Battery Company Home page</a><a href='battery_company Summary.html'>Battery company Summary</a></nav>");
			    outputStream.println("");
			    outputStream.println("</p>");
			    outputStream.println("<div>");
				outputStream.println("<p>");
				
				
				// ************************ //
				// ADD VALUES INTO ACCOUNTS //
				// ************************ //
				System.out.println("***************Beginning of transaction" + numCounter+"************************");
				
				outputStream.println("<p>*************Beginning of transaction"+ numCounter+"**********</p>");
				
				
				double bal = Double.parseDouble(values[3]);
				System.out.println("The income for the date " + values[2] + " is: " 
						+ bal);
				
				outputStream.println("<p>The income for the date " + values[2] + " is: " 
						+ bal+"</p>");
				
				if (numCounter >= 2)
				{
					accountBalance = bal + getAccountBalance( remainingBalance );
					
					cttaxcollected = totalCtTaxCollected(cttaxcollected, newTotalcttaxcollected);
					njtaxcollected = totalNjTaxCollected(njtaxcollected, newTotalnjtaxcollected);
					nytaxcollected = totalNyTaxCollected( nytaxcollected, newTotalnytaxcollected);
				}
				
				
				accountBalance = accountBalance + bal;
				System.out.println("\n The account balance is : " + accountBalance);
				
				outputStream.println("<p>\n The account balance is : " + accountBalance+"</p>");
				
				double escobal = Double.parseDouble(values[5]);
				escoBalance = escoBalance + escobal;
				
				System.out.println("The tax collected for the date " + values[2] + " is: " 
						+ escobal);
				
				outputStream.println("<p>The tax collected for the date " + values[2] + " is: " 
						+ escobal+"</p>");
				
				double expenses = Double.parseDouble(values[4]);
				accountBalance = accountBalance - expenses;
				
				
				System.out.println("The expenses for the date " + values[2] + " is: " 
						+ expenses);
				
				outputStream.println("<p>The expenses for the date " + values[2] + " is: " 
						+ expenses+"</p>");
				
				System.out.println("The new account balance is :"+ accountBalance);
				
				outputStream.println("<p>The new account balance is :"+ accountBalance+"</p>");
				
				// ******************************************************************** //
				// DEPOSIT AMOUNTS INTO EACH ACCOUNT CHECKING AND ESCO PER EACH COMPANY //
				// ******************************************************************** //
				accountBalance = getAccountBalance(accountBalance);
				double newAccountBalance = depositInChecking(accountBalance, bal);
				
				System.out.println("The new account balance is: " + newAccountBalance);
				outputStream.println("<p>The new account balance is: " + newAccountBalance+"</p>");
				
                System.out.println("***************END of transaction" + numCounter+"************************");
				
				outputStream.println("<p>*************END of transaction"+ numCounter+"**********</p>");
				if ( values[1] == "NY")
				{
				       newTotalnytaxcollected = nytaxcollected + Double.parseDouble(values[5]);
				       
				       System.out.println("the amount of total ny tax collected is: " +
				       newTotalnytaxcollected);
				       
				       outputStream.println("<p>the amount of total ny tax collected is: " +
						       newTotalnytaxcollected+"</p>");
				}
				else if (values[1] == "NJ")
				{
					newTotalnjtaxcollected = njtaxcollected + Double.parseDouble(values[5]);
					
					System.out.println("the amount of NJ tax collected is: "+ 
					newTotalnjtaxcollected);
					
					outputStream.println("<p>the amount of NJ tax collected is: "+ 
							newTotalnjtaxcollected+ "</p>");
				}
				else if (values[1] == "CT")
				{
					newTotalcttaxcollected = cttaxcollected + Double.parseDouble(values[5]);
					
					System.out.println("the amount of CT tax collected is: " + 
					newTotalcttaxcollected);
					
					outputStream.println("<p>the amount of CT tax collected is: " + 
							newTotalcttaxcollected+"</p>");
				}else if (values[1] == "BOSTON")
				{
					newTotalBostonTaxCollected = bostonTaxCollected + Double.parseDouble(values[5]);
					
					System.out.println("the amount of BOSTON tax collected is: " + 
							newTotalBostonTaxCollected);
					
					outputStream.println("<p>the amount of CT tax collected is: " + 
							newTotalBostonTaxCollected+"</p>");
				}else if (values[1] == "CHICAGO")
				{
					newTotalChicagoTaxCollected = chicagoTaxCollected + Double.parseDouble(values[5]);
					
					System.out.println("the amount of Chicago tax collected is: " + 
							newTotalChicagoTaxCollected);
					
					outputStream.println("<p>the amount of Chicago tax collected is: " + 
							newTotalChicagoTaxCollected+"</p>");
				}
				
				
				
				escoBalance = getEscoBalance(escoBalance);
				double newEscoBalance = depositInEsco(escoBalance, escobal);
				
				accountBalance = getAccountBalance(accountBalance);
				double newAccountBalance1 = depositInChecking(accountBalance, bal);
				
				expenses = getExpenses(expenses);
				double remainingBalance = newAccountBalance1 - expenses;
				
				
                System.out.println("***************Beginning of Statement for Transaction " + numCounter+"************************");
				
				outputStream.println("<p>*************Beginning of Statement for Transaction "+ numCounter+"**********</p>");
				
				System.out.println("The new account balance minus total "+ expenses 
						+ " in expenses is " + remainingBalance);
				
				outputStream.println("<p>The new account balance minus total "+ expenses 
						+ " in expenses is " + remainingBalance+"</p>");
				
				System.out.println("The new Esco balance is: " + newEscoBalance);
				outputStream.println("<p>The new Esco balance is: " + newEscoBalance+"</p>");

				System.out.println(" the total new york tax collected is: " + nytaxcollected);
				outputStream.println("<p>the total new york tax collected is: " + nytaxcollected+"</p>" );
				
				System.out.println(" the total CT tax collected is: " + cttaxcollected);
				outputStream.println("<p>the total CT tax collected is: " + cttaxcollected+"</p>" );
				
				System.out.println(" the total New Jersey tax collected is: " + njtaxcollected);
				outputStream.println("<p>the total New Jersey tax collected is: " + njtaxcollected+"</p>" );
				
				System.out.println(" the total BOSTON tax collected is: " + bostonTaxCollected);
				outputStream.println("<p>the total BOSTON tax collected is: " + bostonTaxCollected+"</p>" );
				
				System.out.println(" the total CHICAGO tax collected is: " + chicagoTaxCollected);
				outputStream.println("<p>the total CHICAGO tax collected is: " + chicagoTaxCollected+"</p>" );
				
                System.out.println("***************END of Statement "+numCounter+"************************");
				
				outputStream.println("<p>*************END of Statement "+ numCounter + "**********************</p>");

				
				//ending html page statements
				outputStream.println("</p>");
				outputStream.println("</div>");
				outputStream.println(" <nav><a href='mainpage.html'>Main page</a><a href='battery_company Home.html'>Battery Company Home page</a> <a href='battery_company Summary.html'>Battery company Summary</a> </nav> ");
				outputStream.println("               </body>");
				outputStream.println("        </html>");
	            outputStream.close();
			}
			
					/*
			System.out.println(" the total new york tax collected is: " + nytaxcollected);
			outputStream.println("the total new york tax collected is: " + nytaxcollected );
			
			System.out.println(" the total CT tax collected is: " + cttaxcollected);
			outputStream.println("the total CT tax collected is: " + cttaxcollected );
			
			System.out.println(" the total New Jersey tax collected is: " + njtaxcollected);
			outputStream.println("the total New Jersey tax collected is: " + njtaxcollected );
			
			System.out.println(" the total BOSTON tax collected is: " + bostonTaxCollected);
			outputStream.println("the total BOSTON tax collected is: " + bostonTaxCollected );
			
			System.out.println(" the total CHICAGO tax collected is: " + chicagoTaxCollected);
			outputStream.println("the total CHICAGO tax collected is: " + chicagoTaxCollected );
			
			*/
			inputStream.close();
			
		} catch(FileNotFoundException e){
			e.printStackTrace();
		}
		}//end main
	
	

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
		
		//getter for ny tax collected
		public static double totalNyTaxCollected( double nytaxcollected, double prevamount){
			nytaxcollected = nytaxcollected + prevamount;
			return nytaxcollected;
		}
		
		//getter for nj tax collected
		public static double totalNjTaxCollected(double njtaxcollected, double prevamount){
			njtaxcollected = njtaxcollected + prevamount;
			return njtaxcollected;
		}
		// getter for ct tax collected
		public static double totalCtTaxCollected(double cttaxcollected, double prevamount){
			cttaxcollected = cttaxcollected + prevamount;
			return cttaxcollected;
		}


	
	
}