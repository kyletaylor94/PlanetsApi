//
//  SolarSystemApiPracticeMVVMApp.swift
//  SolarSystemApiPracticeMVVM
//
//  Created by Turdesán Csaba on 2023. 04. 02..
//

import SwiftUI

@main
struct SolarSystemApiPracticeMVVMApp: App {
    var network = Network()
    var body: some Scene {
        WindowGroup {
            ContentView().environmentObject(network)
        }
    }
}
