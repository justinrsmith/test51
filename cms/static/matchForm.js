var MatchForm = React.createClass({
    getInitialState: function(){
        return {
            selectedGameId: 0,
            selectedCompetitionId: 0,
            team1: 0,
            team2: 0,
            results: []
        }
    },
    componentDidMount: function(){
        this.fetchGames()
    },
    addResult: function(){
        var results = this.state.results
        var id = results.length + 1
        results.push({id: {}})
        this.setState({results: results})
    },
    fetchCompetitions: function(url){
        var that = this
        getJSON(url, {
            success: that.parseCompetitions
        })
    },
    fetchGames: function(){
        var that = this
        getJSON('/api/games', {
            success: that.parseGames
        })
    },
    fetchTeams: function(url){
        var that = this
        getJSON(url, {
            success: that.parseTeams
        })
    },
    parseCompetitions: function(d){
        this.setState({competitions: d, selectedCompetitionId: d[0].id})
        this.fetchTeams('/api/teams/')
    },
    parseGames: function(d){
        this.setState({
            games: d,
            selectedGameId: d[0].id,
            selectedGame: d[0]
        })
        this.fetchCompetitions('/api/competitions/?game='+this.state.selectedGameId)
    },
    parseTeams: function(d){
        this.setState({teams: d})
    },
    saveMatch: function(){
        console.log(this.state.date)
        var final_data = {}
        final_data['competition'] = this.state.selectedCompetitionId
        final_data['date'] = this.state.date
        console.log(this.state.results)
        /*var i = 0
        while(true){
            console.log()
        }*/

        var data ={
            "matchmap_set": [
                {
                    "matchmapteamresult_set": [
                        {
                            "first_half_score": 3,
                            "second_half_score": 9,
                            "overtime_score": 0,
                            "match_map": 1,
                            "team": 7,
                            "fielded_roster": [
                                5
                            ]
                        },
                        {
                            "first_half_score": 3,
                            "second_half_score": 13,
                            "overtime_score": 0,
                            "match_map": 1,
                            "team": 8,
                            "fielded_roster": [
                                6
                            ]
                        }
                    ],
                    "map": 1
                },
                {
                    "matchmapteamresult_set": [
                    	{
                            "first_half_score": 3,
                            "second_half_score": 9,
                            "overtime_score": 0,
                            "match_map": 2,
                            "team": 7,
                            "fielded_roster": [
                                5
                            ]
                        },
                        {
                            "first_half_score": 3,
                            "second_half_score": 13,
                            "overtime_score": 0,
                            "match_map": 2,
                            "team": 8,
                            "fielded_roster": [
                                6
                            ]
                        }
                    ],
                    "map": 2
                },
                {
                    "matchmapteamresult_set": [],
                    "map": 4
                }
            ],
            "date": "2017-02-09",
            "competition": 1
        }
        /*var that = this
        request('/api/matches/', {
            method: 'POST',
            alterRequest: function(r){
                r.setRequestHeader('content-type', 'application/json')
                r.setRequestHeader('X-CSRFToken', that.props.csrf)
                return r
            },
            data: JSON.stringify(data),
            success: function(){
                conosle.log('hi')
            }
        })*/
    },
    setDate: function(e){
        console.log(e.target.value)
        this.setState({date: e.target.value})
    },
    setGame: function(e){
        var selectedGame= this.state.games.filter(function(obj){
            if(obj.id==e.target.value)
                return obj
        })[0]
        this.setState({
            selectedGameId: e.target.value,
            selectedGame: selectedGame
        })
        this.fetchCompetitions('/api/competitions/?game='+e.target.value)
    },
    setTeam1: function(e){
        // Get the team object
        var selectedTeam = this.state.teams.filter(function(obj){
            if(obj.id==e.target.value)
                return obj
        })[0] //should only match on 1
        console.log(selectedTeam)
        this.setState({
            selectedTeam1: selectedTeam
        })
    },
    setTeam2: function(e){
        // Get the team object
        var selectedTeam = this.state.teams.filter(function(obj){
            if(obj.id==e.target.value)
                return obj
        })[0] //should only match on 2

        this.setState({
            selectedTeam2: selectedTeam
        })
    },
    setMap: function(i){
        console.log(this.state.results[i])
        this.state.results[i].map = this.refs['map-'+i].value
        console.log(this.state.results[i])
        console.log(this.refs['map-'+i].value)
//console.log(e, i)
    },
    render: function(){
        var that = this
        return div(
            !that.state.teams?null:
            div({className: 'col-md-6 col-md-offset-3'},
                div({className: 'row'}, label('Game'),
                    // Game select
                    select({
                        className: 'form-control',
                        key: 'game-select',
                        onChange: this.setGame,
                        value: this.state.selectedGameId
                    },
                        that.state.games.map(function(k, v){
                            return option({key: 'game-opt-'+v, value:k.id}, k.name)
                        })
                    )
                ),
                div({className: 'row'}, label('Competition'),
                    // Competition select
                    // Populates based on game selection
                    select({
                        key: 'competition-select',
                        className: 'form-control'
                    },
                        that.state.competitions.map(function(k, v){
                            return option({key: 'comp-opt-'+v, value:k.id}, k.name)
                        })
                    )
                ),
                div({className: 'row'}, label('Date'),
                    // Competition select
                    // Populates based on game selection
                    input({
                        className: 'form-control',
                        type: 'date',
                        onChange: this.setDate
                    })
                ),
                div({className: 'row'}, label('Team 1'),
                    // Team select
                    // Gets roster when a team is selected
                    select({
                        key: 'team1-select',
                        className: 'form-control',
                        onChange: this.setTeam1,
                        value: this.state.selectedTeamId
                    },option(),
                        that.state.selectedGame.team_set.map(function(k, v){
                            return option({key: 'team1-opt-'+v, value:k.id}, k.name)
                        })
                    )
                ),
                !this.state.selectedTeam1?null:div({className: 'row'}, label('Team 1 Roster'),
                    select({
                        key: 'team1-roster-select',
                        className: 'form-control',
                        multiple: true
                    },
                        that.state.selectedTeam1.teamplayer_set.map(function(k, v){
                            if(k.active)
                                return option({key: 'team1-player-opt-'+v, value:k.player.id}, k.player.handle)
                        })
                    )
                ),
                div({className: 'row'}, label('Team 2'),
                    // Team select
                    // Gets roster when a team is selected
                    select({
                        key: 'team2-select',
                        className: 'form-control',
                        onChange: this.setTeam2,
                        value: this.state.selectedTeamId
                    },option(),
                        that.state.selectedGame.team_set.map(function(k, v){
                            return option({key: 'team2-opt-'+v, value:k.id}, k.name)
                        })
                    )
                ),
                !this.state.selectedTeam2?null:div({className: 'row'}, label('Team 2 Roster'),
                    select({
                        key: 'team2-roster-select',
                        className: 'form-control',
                        multiple: true
                    },
                        that.state.selectedTeam2.teamplayer_set.map(function(k, v){
                            if(k.active)
                                return option({key: 'team2-roster-opt-'+v, value:k.player.id}, k.player.handle)
                        })
                    )
                ),
                div({className: 'row'},
                    // Team select
                    // Gets roster when a team is selected
                    a({
                        className: 'btn btn-primary',
                        onClick: this.addResult
                    }, 'Add a Result')
                ),
                div({className: 'row'},
                    // Team select
                    // Gets roster when a team is selected
                    a({
                        className: 'btn btn-primary',
                        onClick: this.saveMatch
                    }, 'Save Match')
                ),
                !this.state.results.length?null:
                    table({className: 'table'},
                        thead(
                            tr(
                                th('Map'),
                                th('Team 1 Score'),
                                th('Team 2 Score')
                            )
                        ),
                        tbody(
                            this.state.results.map(function(obj, i){
                                return tr(
                                    td(
                                        select({
                                            key: 'team2-roster-select',
                                            className: 'form-control',
                                            onChange: that.setMap.bind(that, i),
                                            ref: 'map-'+i
                                        },
                                            that.state.selectedGame.map_set.map(function(k, v){
                                                return option({key: 'map-opt-'+v, value:k.id}, k.name)
                                            })
                                        )
                                    ),
                                    td(
                                        input({
                                            className: 'form-control',
                                            placeholder: '1st Half',
                                            ref: 'team1-first_half-'+i,
                                            style: {
                                                'width': '100px'
                                            }
                                        }),
                                        input({
                                            className: 'form-control',
                                            placeholder: '2nd Half',
                                            ref: 'team1-second_half-'+i,
                                            style: {
                                                'width': '100px'
                                            }
                                        }),
                                        input({
                                            className: 'form-control',
                                            placeholder: 'Overtime',
                                            ref: 'team1-overtime-'+i,
                                            style: {
                                                'width': '100px'
                                            }
                                        })
                                    ),
                                    td(
                                        input({
                                            className: 'form-control',
                                            placeholder: '1st Half',
                                            ref: 'team2-first_half-'+i,
                                            style: {
                                                'width': '100px'
                                            }
                                        }),
                                        input({
                                            className: 'form-control',
                                            placeholder: '2nd Half',
                                            ref: 'team2-second_half-'+i,
                                            style: {
                                                'width': '100px'
                                            }
                                        }),
                                        input({
                                            className: 'form-control',
                                            placeholder: 'Overtime',
                                            ref: 'team2-overtime-'+i,
                                            style: {
                                                'width': '100px'
                                            }
                                        })
                                    )
                                )
                            })
                        )
                    )
            )
        )
    }
})
