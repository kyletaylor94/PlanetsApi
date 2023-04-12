//
//  DescriptionView.swift
//  SolarSystemApiPracticeMVVM
//
//  Created by Turdesán Csaba on 2023. 04. 02..
//

import SwiftUI

struct DescriptionView: View {
    
    var planet: Planets?
    
    var body: some View {
        
        ScrollView {
            VStack{
                if let planet = planet{
                    AsyncImage(url: URL(string: "\(planet.image)")) { image in
                        image
                            .resizable()
                            .aspectRatio(contentMode: .fill)
                        
                    } placeholder: {
                        ProgressView()
                    }.frame(width: 100, height: 100)
                        .cornerRadius(30)
                    
                    Text(planet.name)
                        .font(Font.title)
                        .foregroundColor(.black)
                        .bold()
                        .multilineTextAlignment(.trailing)
                        .padding(.top)
                    Text(planet.description)
                        .font(Font.body)
                        .padding()
                    
                    Spacer()
                } else {
                    Text("No Planet selected")
                }
            }
        }
    }
}

struct DescriptionView_Previews: PreviewProvider {
    static var previews: some View {
        DescriptionView()
    }
}
