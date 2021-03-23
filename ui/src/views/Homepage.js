import React, {Component} from 'react';
import {Button, Form} from "react-bootstrap";
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

export default class Homepage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            questions_so_far: [],
            answers_so_far: [],
            question: '',
            question_id: 0,
            prediction: false,
            questionAdd: false,
            techs_left: [],
            techs_so_far: [],
            tech_answers_so_far: [],
            new_question: '',
            techAdd: false,
            questions_left: [],
            new_tech: '',
            techNeeded: true
        }
    }

    componentDidMount() {
        this.init()
    }

    async resetGame() {
        await this.setState({
            questions_so_far: [],
            answers_so_far: [],
            prediction: false,
        })
        this.init()
    }

    init() {
        axios.post('/api/answer', {}).then(r => {
            let question = r.data.question
            let question_id = r.data.question_id

            this.setState({question, question_id})
        })
    }

    async addQuestion(tech = undefined, weight = 0.5) {
        console.log(tech)
        if (tech) {
            let techs_so_far = this.state.techs_so_far
            let tech_answers_so_far = this.state.tech_answers_so_far
            techs_so_far.push(tech)
            tech_answers_so_far.push(weight)
            console.log(techs_so_far, tech_answers_so_far)
            await this.setState({techs_so_far, tech_answers_so_far})
        }
        let answers = {};
        this.state.techs_so_far.forEach((key, i) => answers[key] = this.state.tech_answers_so_far[i]);
        console.log(answers)
        axios.post('/api/add/question', {question: this.state.new_question, answers}).then(r => {
            if (r.data.techs) {
                let techs_left = r.data.techs.filter(n => !this.state.techs_so_far.includes(n))
                this.setState({
                    techs_left,
                    questionAdd: true,
                    prediction: false
                })
            } else {
                this.setState({
                    questionAdd: false,
                    new_question: '',
                    tech_answers_so_far: [],
                    techs_so_far: []
                })
                alert(r.data.message)

            }
        })
    }

    startQuestionAdd() {
        this.setState({questionAdd: true, prediction: false})
    }

    startAddTech() {
        this.setState({techAdd: true, prediction: false})
    }

    async addTech(question = undefined, weight = 0.5) {
        if (question) {
            let questions_so_far = this.state.questions_so_far
            let answers_so_far = this.state.answers_so_far
            questions_so_far.push(question)
            answers_so_far.push(weight)
            console.log(questions_so_far, answers_so_far)
            await this.setState({questions_so_far, answers_so_far})
        }
        let answers = {};
        this.state.questions_so_far.forEach((key, i) => answers[key] = this.state.answers_so_far[i]);
        axios.post('/api/add/tech', {name: this.state.new_tech, answers}).then(r => {
            let questions_left = r.data.questions_left
            console.log(questions_left)
            if (questions_left) {
                this.setState({
                    questions_left,
                    techNeeded: false
                })
            } else {
                this.setState({
                    techAdd: false,
                    new_tech: '',
                    answers_so_far: [],
                    questions_so_far: []
                })
                alert(r.data.message)
            }
        })
    }

    updateQuestion(new_question) {
        this.setState({new_question})
    }

    updateTech(new_tech) {
        this.setState({new_tech})
    }

    async answerQuestion(weight) {
        let answers_so_far = this.state.answers_so_far
        let questions_so_far = this.state.questions_so_far
        answers_so_far.push(weight)
        questions_so_far.push(this.state.question_id)
        await this.setState({answers_so_far})
        axios.post('/api/answer', {answers_so_far, questions_so_far}).then(r => {
            let prediction = r.data.prediction
            let question = r.data.question
            let question_id = r.data.question_id
            if (prediction) {
                this.setState({prediction})
            } else {
                this.setState({question, question_id, questions_so_far})
            }
        })
    }

    render() {
        return(
            <>
                {(!this.state.prediction && !this.state.questionAdd && !this.state.techAdd) && (
                    <>
                        <h2>{this.state.question}</h2>
                        <Button variant={'outline-secondary'} onClick={() => {this.answerQuestion(1)}}>Yes</Button><br />
                        <Button variant={'outline-secondary'} onClick={() => {this.answerQuestion(0.75)}}>Probably</Button><br />
                        <Button variant={'outline-secondary'} onClick={() => {this.answerQuestion(0.5)}}>Don't know/Not applicable</Button><br />
                        <Button variant={'outline-secondary'} onClick={() => {this.answerQuestion(0.25)}}>Probably not</Button><br />
                        <Button variant={'outline-secondary'} onClick={() => {this.answerQuestion(0)}}>No</Button>
                    </>
                )}
                {this.state.prediction && (
                    <>
                        <h2>{this.state.prediction}</h2>
                        <Button variant={'outline-secondary'} onClick={() => {this.resetGame()}}>Restart</Button><br />
                        <h4>Not correct?</h4>
                        <Button variant={'outline-secondary'} onClick={() => {this.addQuestion()}}>Add a new question</Button><br />
                        <Button variant={'outline-secondary'} onClick={() => {this.startAddTech()}}>Use the questions you've already answered to add a new tech</Button>
                    </>
                )}
                {this.state.questionAdd && (
                    <>
                        <Form.Control placeholder={'Type question here...'} value={this.state.new_question} onChange={(e) => this.updateQuestion(e.target.value)} />
                        {this.state.new_question && (
                            <>
                                {this.state.techs_left.map(e => (
                                        <>
                                            <h2>{this.state.new_question} - {e}</h2>
                                            <Button variant={'outline-secondary'} onClick={() => {this.addQuestion(e,1)}}>Yes</Button><br />
                                            <Button variant={'outline-secondary'} onClick={() => {this.addQuestion(e,0.75)}}>Probably</Button><br />
                                            <Button variant={'outline-secondary'} onClick={() => {this.addQuestion(e,0.5)}}>Don't know/Not applicable</Button><br />
                                            <Button variant={'outline-secondary'} onClick={() => {this.addQuestion(e,0.25)}}>Probably not</Button><br />
                                            <Button variant={'outline-secondary'} onClick={() => {this.addQuestion(e,0)}}>No</Button>
                                        </>
                                    )
                                )}
                            </>
                        )}
                    </>
                )}
                {this.state.techAdd && (
                    <>
                        <Form.Control placeholder={'Type technology here...'} value={this.state.new_tech} onChange={(e) => this.updateTech(e.target.value)} />
                        {this.state.techNeeded && (
                            <>
                                <Button variant={'outline-secondary'} onClick={() => {this.addTech()}}>Done</Button>
                            </>
                        )}
                        {this.state.new_tech && (
                            <>
                                {this.state.questions_left.map(e => (
                                    <>
                                        <h2>{this.state.new_tech} - {e.question}</h2>
                                        <Button variant={'outline-secondary'} onClick={() => {this.addTech(e.question_id,1)}}>Yes</Button><br />
                                        <Button variant={'outline-secondary'} onClick={() => {this.addTech(e.question_id,0.75)}}>Probably</Button><br />
                                        <Button variant={'outline-secondary'} onClick={() => {this.addTech(e.question_id,0.5)}}>Don't know/Not applicable</Button><br />
                                        <Button variant={'outline-secondary'} onClick={() => {this.addTech(e.question_id,0.25)}}>Probably not</Button><br />
                                        <Button variant={'outline-secondary'} onClick={() => {this.addTech(e.question_id,0)}}>No</Button>
                                    </>
                                ))}
                            </>
                        )}
                    </>
                )}
            </>
        )
    }
}