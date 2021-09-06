import Nav from './components/Nav'
import MainPage from './components/MainPage'
import Statistics from './components/Statistics'
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'
function App() {
  return (
    <Router>
      <div className = "App">
        <header className="App-header">
          <Nav />
          <Switch>
            <Route path = "/" exact component={MainPage} />
            <Route path = "/statistics" component = {Statistics} />
          </Switch>
        </header>
      </div>
    </Router>
  );
}

export default App;
