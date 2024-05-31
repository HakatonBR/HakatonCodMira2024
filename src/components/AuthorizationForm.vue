<script>
import axios from 'axios';
import Footer from './Footer.vue';
import Header from './Header.vue';

export default{
    components: {
        Header,
        Footer,
        axios
    },
    props: {
        logo_name: {
            type: String,
            required: true
        },
    },
    data() {
        return {
            show_password: false,
            user_info: {
                email: "",
                password: "",
            },
            rules: {
                emailMatch: v => /\S+@\S+\.\S+/.test(v) || "Некорректная почта",
                emailDontExist: v => /\S+@\S+\.\S+/.test(v) || "Почты не существует",
                authFail: v => /\S+@\S+\.\S+/.test(v) || "Неверный логин или пароль",
            }
            }
    },
    methods: {
        authorization(){
            // axios.post(`#`, [this.user_info]) // add the link
        },
    }

}
</script>

<template>
    <Header :logo_name="this.logo_name"></Header>
    <v-container fluid class="container">
        <v-form class="registration-form">
            <img src="" alt="" class="registration-logo"> 
            <h1 class="registration-title">
                Авторизация
            </h1>
            <hr class="registration-divider">
            <v-text-field 
                prepend-inner-icon="mdi-email-outline"
                v-model="this.user_info.email"
                type="email" 
                :rules="[rules.emailMatch]"
                class="registration-row-input" 
                label="Email"
                required 
            ></v-text-field>
            <v-text-field 
                :append-inner-icon="show_password ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show_password ? 'text' : 'password'"
                counter
                @click:append-inner="show_password = !show_password"
                prepend-inner-icon="mdi-lock-outline"
                class="registration-row-input" 
                label="Пароль" 
                required 
                v-model="this.user_info.password"
                :rules="[rules.passwordMatch]"
            ></v-text-field>
            <v-btn type="submit" class="registration-submit" @click="register()" block>Авторизоваться</v-btn>
            <p class="register-signin">
                <pre>У вас нет аккаунта? <a href="#" class="register-signin-url">Зарегистрируйтесь</a></pre>
            </p>
        </v-form>
    </v-container>
    <Footer :logo_name="this.logo_name"></Footer>
</template>

<style scoped>

.container{
    justify-content: center;
    align-items: center;
    width: 100%;
}

.registration-title{
    margin: 10px;
    font-size: 30px;
}

a{
    color: #ff96a6;
    text-decoration: none;
}

a:hover{
    color: 1px solid #fd6e8c;
    translate: 300ms;
}

.registration-divider{
    margin-top: 20px;
    justify-content: center;
    height: 4px;
    width: 100px;
    background-color: #ff96a6;
    border: none;
}

.registration-form{
    margin-top: 50px;
    padding: 30px;
    border-radius: 50px;
    background-color: #fdf0f0;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 576px;
}

.registration-row-input{
    width: 500px;
    margin-top: 30px;
}

.register-signin{
    text-align: center;
    display: block;
}

.registration-submit{
    margin-top: 50px;
    margin-bottom: 30px;
    cursor: pointer;
    padding: 10px;
    border-radius: 30px;
    color: white;
    background-color: #ff96a6;
    border: none;
    height: 60px;
    width: 100%;
}

.registration-submit:hover{
    background-color: #fd6e8c;
    transition: 300ms;
} 
</style>