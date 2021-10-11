import os, requests

def get_tournament_info(page, per_page, tournament_slug):
  return requests.post(
    "https://api.smash.gg/gql/alpha", 
    headers= { 
      "Accept": "application/json", 
      "Authorization": "Bearer {}".format(os.environ['SMASHGG_TOKEN'])
    },
    json= {
      'query': """query GetTournamentInfo($slug: String, $page: Int!, $perPage: Int!) {
        tournament(slug: $slug) {
          id
          name
          events {
            id
            name
            phases{
              id
              name
            }
            standings(query: {
            perPage: $perPage,
            page: $page
          }){
            nodes {
              placement
              entrant {
                id
                name
                participants{
                  id
                  gamerTag
                  player{
                    id
                    gamerTag
                    user{
                      id
                      name
                      discriminator
                    }
                  }
                }
              }
            }
          }
          }
        }
      }""", 
      'variables': { "page": page, "perPage": per_page, "slug": tournament_slug }
    }
  )

def get_results_info(page, per_page, event_id):
  return requests.post(
    "https://api.smash.gg/gql/alpha", 
    headers= { 
      "Accept": "application/json", 
      "Authorization": "Bearer {}".format(os.environ['SMASHGG_TOKEN'])
    },
    json= {
      'query': """query GetResultsInfo($eventId: ID!, $page: Int!, $perPage: Int!) {
        event(id: $eventId) {
          name
          phases{
            id
            name
            sets(page: $page, perPage: $perPage, sortType: STANDARD) {
              nodes {
                winnerId
                slots {
                  entrant {
                    id
                    name
                  }
                }
              }
            }
          }
        }
      }""", 
      'variables': { "page": page, "perPage": per_page, "eventId": event_id }
    }
  )