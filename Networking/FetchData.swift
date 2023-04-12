//
//  FetchData.swift
//  SolarSystemApiPracticeMVVM
//
//  Created by Turdesán Csaba on 2023. 04. 02..
//

import Foundation

class Network: ObservableObject {
    @Published var planets: [Planets] = []
    
    init(){
        fetchPlanets()
    }
    
    func fetchPlanets(){
        
        guard let endpoint = URL(string: "http://127.0.0.1:5000/solarsystem") else {
            fatalError("Missing URL")}
        
        let decoder = JSONDecoder()
        
        let request = URLRequest(url: endpoint)
        
        let dataTask = URLSession.shared.dataTask(with: request){ data, response, error in
            if let error = error {
                print("Request error: \(error)")
                return
            }
            guard let response = response as? HTTPURLResponse else { return }
            
            if response.statusCode == 200{
                guard let data = data else { return }
                DispatchQueue.main.async {
                    do{
                        let decodedPlanets = try decoder.decode([Planets].self, from: data)
                        self.planets = decodedPlanets
                        
                    } catch let error{
                        print("error with decoding: \(error)")
                    }
                }
            }
        }
        dataTask.resume()
    }
}
