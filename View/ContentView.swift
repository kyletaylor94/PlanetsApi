//
//  ContentView.swift
//  SolarSystemApiPracticeMVVM
//
//  Created by Turdesán Csaba on 2023. 04. 02..
//

import SwiftUI

struct ContentView: View {
    @EnvironmentObject var network: Network
    
    @State var selectedPlanet : Planets?
    
    var body: some View {
        
        NavigationView{
        List(network.planets){ planet in
            Button {
                selectedPlanet = planet
                print(selectedPlanet?.name)
                    } label: {
                    HStack(spacing: 70){
                        AsyncImage(url: URL(string: "\(planet.image)")) { image in
                            image
                                .resizable()
                                .aspectRatio(contentMode: .fill)
                            
                        } placeholder: {
                            ProgressView()
                        }.frame(width: 100, height: 100)
                            .cornerRadius(30)
                        
                        Text(planet.name)
                            .font(Font.title2)
                            .foregroundColor(.black)
                            .bold()
                        
                    }
                    .alignmentGuide(.listRowSeparatorLeading) { viewDimensions in
                        return 0
                    }
                }
                .background(NavigationLink(destination: DescriptionView(planet: selectedPlanet)) {
                              EmptyView()
                    })
            }
        .listStyle(.inset)
        }
    }
}
    
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView().environmentObject(Network())
    }
}


