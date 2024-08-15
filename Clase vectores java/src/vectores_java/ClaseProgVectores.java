/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package vectores_java;

import  java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
public class ClaseProgVectores {

    
    public static void main(String[] args) {
     
        String Vacio [] = {};
        System.out.println("Lista Vacia" + Arrays.deepToString(Vacio));
        
        String Elem [] = {"Mariposa" , "Aranha" , "Murcielago" , "Conejo" , "Espantapajaro"};
        System.out.println("Lista Con Elementos" + Arrays.deepToString(Elem));
        
        System.out.println("Longitud: " + " " + Elem.length);
        
        System.out.println("\nObtencion De Elementos: ");
        System.out.println("Primer Elemento: " + " " + Elem[0]);
        System.out.println("Segundo Elemento:" + " " + Elem[2]);
        System.out.println("Tercer Elemento:" + " " + Elem[4]);
        
        System.out.println("\nDatos Personales");
        ArrayList<String>Datos_Personales = new ArrayList();
        Datos_Personales.add("Manuel");
        Datos_Personales.add("18");
        Datos_Personales.add("1.75");
        Datos_Personales.add("Soltero");
        Datos_Personales.add("#####");
        Datos_Personales.add("Estudiante");
        System.out.println(Datos_Personales);
        
        System.out.println("\nEmpresa It Companies");
        ArrayList<String>It_Companies = new ArrayList();
        It_Companies.add("Facebook");
        It_Companies.add("Google");
        It_Companies.add("Microsoft");
        It_Companies.add("Apple");
        It_Companies.add("IBM");
        It_Companies.add("Oracle");
        It_Companies.add("Amazon");
        It_Companies.add("Kwai");
        It_Companies.add("Tik Tok");
        System.out.println(It_Companies);
        System.out.println("\nValor A comprobar: " + It_Companies.contains("Google"));
        
        Collections.sort(It_Companies);
        System.out.println("\nValores Ordenados" + It_Companies);
        
        System.out.println("\nInvirtiendo Lista: ");
        Collections.reverse(It_Companies);
        System.out.println(It_Companies);
        
        
        It_Companies.remove(0);
        System.out.println("\nEliminacion De La Primera Empresa:" + It_Companies);
        
        It_Companies.clear();
        System.out.println("\nLista Limpiada: "+ It_Companies);
        
        
        
        
        
       
        
    }
    
}
