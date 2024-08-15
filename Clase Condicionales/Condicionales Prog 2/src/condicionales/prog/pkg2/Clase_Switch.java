/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package condicionales.prog.pkg2;

import java.util.Scanner;

public class Clase_Switch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        char numero;
        
        
        System.out.println("Elija una opcion");
        
        System.out.println("Menu");
        System.out.println("\n1.Personas");
        System.out.println("2.vehiculos");
        System.out.println("3.universidades");
        System.out.println("4.notas");
        System.out.println("5.salir");
        
        
        System.out.println("Ingrese un numero: ");
        numero = sc.next().charAt(0);
        
        switch(numero){
            case '1':
                System.out.println("Elegiste la opcion" + " " + "Personas");
                break;
                
            case '2':
                System.out.println("Elegiste la opcion" + " " + "Vehiculos");
                break;
                
            case'3':
                System.out.println("Elegiste la opcion" + " " + "universidades");
                break;
                
            case'4':
                System.out.println("Elegiste la opcion" + " " + "notas");
                break;
                
            case'5':
                System.out.println("Elegiste la opcion" + " " + "salir");
                break;
                
            default: System.out.println("Numero no valido");
        }
        
    }
    
}
