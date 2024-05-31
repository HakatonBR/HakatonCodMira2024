<script>
import Footer from './components/Footer.vue';
import Header from './components/Header.vue';

export default{
    components: {
        Header,
        Footer,
    },
}
</script>

<template>
    <v-app>
        <Header/>
        <RouterView/>
        <Footer/>
    </v-app>
</template>