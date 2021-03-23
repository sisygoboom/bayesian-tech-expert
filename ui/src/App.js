import './App.css';
import Homepage from "./views/Homepage";
import {Container} from "react-bootstrap";

function App() {
  return (
    <div className="App">
      <header className="App-header">
          <Container>
              <Homepage />
          </Container>
      </header>
    </div>
  );
}

export default App;
