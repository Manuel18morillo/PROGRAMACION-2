/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.personas;

/**
 *
 * @author Sala de Sistemas
 */
public class Personas {

    public static void main(String[] args) {
        
        PersonaManuel P = new PersonaManuel();
        P.setNombre("Manuel");
        System.out.println(P.getNombre());
        
        P.setApellidos("Morillo");
        System.out.println(P.getApellidos());
        
        P.setCorreo("morillomanuel502@gmail.com");
        System.out.println(P.getCorreo());
        
        P.setCedula(1234567890);
        System.out.println(P.getCedula());
        
           
    }
}
