<template>
    <div class="col-md-6">
        <h4>Login</h4>
                 <div class="fill-row">
                  <div id="div-with-loading" class="vs-con-loading__container">
                      <form @submit.prevent="login">
                          <div class="form-group">
                          <label for="username">Username</label>
                          <input type="text" v-model="username" name="username" class="form-control" :class="{ 'is-invalid': submitted && !username }" />
                          <div v-show="submitted && !username" class="invalid-feedback">Username is required</div>
                          </div>
                          <div class="form-group">
                              <label htmlFor="password">Password</label>
                              <input type="password" v-model="password" name="password" class="form-control" :class="{ 'is-invalid': submitted && !password }" />
                              <div v-show="submitted && !password" class="invalid-feedback">Password is required</div>
                          </div>
                          <div class="form-group">
                              <button class="btn btn-primary" @click="login" :disabled="this.$store.isLoggedIn">Login</button>
                              <img v-show="this.$store.isLoggedIn" src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />
                              <router-link to="/register" class="btn btn-link">Register</router-link>
                          </div>
                      </form>

                  </div>
                 </div>

    </div>
</template>

<script>

export default {
    data () {
        return {
            submitted: false,
            username:'',
            password:'',
        }
    },
    methods: {
        login: function () {
            const user ={
                username : this.username,
                password : this.password
            }
            this.$store.dispatch('login',user);
        },
    }
};
</script>
