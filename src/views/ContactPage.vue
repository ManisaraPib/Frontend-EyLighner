<template>
    <div>
        <nav-bar></nav-bar>
        <form-contact></form-contact>
        <team-members></team-members>
    </div>
</template>
  
<script>
import NavBar from "../components/NavBar.vue";
import FormContact from "../components/FormContact.vue";
import TeamMembers from "../components/TeamMembers.vue";
export default {
    components: { NavBar, FormContact, TeamMembers },
};
</script>
  
<style>

</style>
  