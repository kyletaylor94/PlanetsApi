//
//  DecodedModel.swift
//  SolarSystemApiPracticeMVVM
//
//  Created by Turdesán Csaba on 2023. 04. 02..
//

import Foundation


struct Planets: Decodable, Identifiable, Hashable {
    var id: Int
    var name: String
    var image: String
    var description: String
}
