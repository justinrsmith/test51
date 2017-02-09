var MatchForm = React.createClass({
    getInitialState: function(){
        return {
            selectedGameId: 0,
            selectedCompetitionId: 0,
            selectedTeam1Id: 0,
            selectedTeam2Id: 0,
            results: []
        }
    },
    componentDidMount: function(){
        this.fetchGames()
    },
    addResult: function(){
        var results = this.state.results
        results.push({})
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

        this.setState({
            selectedTeam1Id:e.target.value,
            team1Players: selectedTeam.players
        })
    },
    setTeam2: function(e){
        // Get the team object
        var selectedTeam = this.state.teams.filter(function(obj){
            if(obj.id==e.target.value)
                return obj
        })[0] //should only match on 2

        this.setState({
            selectedTeam2Id:e.target.value,
            team2Players: selectedTeam.players
        })
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
                            return option({key: 'game-opt-'+v, value:k.id}, k.name+k.id)
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
                !this.state.team1Players?null:div({className: 'row'}, label('Team 1 Roster'),
                    select({
                        key: 'team1-roster-select',
                        className: 'form-control',
                        multiple: true
                    },
                        that.state.team1Players.map(function(k, v){
                            return option({key: 'team1-roster-opt-'+v, value:k.id}, k.handle)
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
                !this.state.team2Players?null:div({className: 'row'}, label('Team 2 Roster'),
                    select({
                        key: 'team2-roster-select',
                        className: 'form-control',
                        multiple: true
                    },
                        that.state.team2Players.map(function(k, v){
                            return option({key: 'team2-roster-opt-'+v, value:k.id}, k.handle)
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
                            this.state.results.map(function(obj){
                                return tr(
                                    td(
                                        select({
                                            key: 'team2-roster-select',
                                            className: 'form-control'
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
                                            style: {
                                                'width': '100px'
                                            }
                                        }),
                                        input({
                                            className: 'form-control',
                                            placeholder: '2nd Half',
                                            style: {
                                                'width': '100px'
                                            }
                                        }),
                                        input({
                                            className: 'form-control',
                                            placeholder: 'Overtime',
                                            style: {
                                                'width': '100px'
                                            }
                                        })
                                    ),
                                    td(
                                        input({
                                            className: 'form-control',
                                            placeholder: '1st Half',
                                            style: {
                                                'width': '100px'
                                            }
                                        }),
                                        input({
                                            className: 'form-control',
                                            placeholder: '2nd Half',
                                            style: {
                                                'width': '100px'
                                            }
                                        }),
                                        input({
                                            className: 'form-control',
                                            placeholder: 'Overtime',
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
