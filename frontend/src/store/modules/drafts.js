import Vue from 'vue';
// single object containing all application level state and serves as single source of truth
const state = {
    drafts:[],
    draft:{}
};

const mutations={
    setDraft : (state,drafts) => {
        state.drafts = drafts;
        console.log(state.drafts)
    },
    setDraftDetail : (state,draft) => {
        state.draft = draft;
    }
};

const actions = {
    readDraft: ({commit }, order) => {
        commit()
    },
    initDrafts :({commit}) => {
        console.log('called draftlist')
        return new Promise((resolve, reject) => {
            Vue.http.get('api/draft/')
            .then(response =>{
                const drafts = response.data;
                console.log(drafts);
                
                commit('setDraft', drafts);
                resolve(response);
            }, error => {
                reject(error);
            });
       })
    },
    initDraftDetail : ({commit},draft) => {
        commit('setDraftDetail',draft);
    },
    publish:({commit,dispatch})=>{
        const id=state.draft.id
    //     return new Promise((resolve, reject) => {
    //         Vue.http.get('api/draft/'+id+'/publish/')
    //         .then(response =>{
    //             const published_draft = response.data;
    //             console.log(published_draft);
    //             resolve(response);
    //         }, error => {
    //             reject(error);
    //         });
    //    })
       dispatch('initPosts')
    }
};

const getters = {
    drafts: state => {
        return state.drafts;
    },
    draftDetail : state => {
        return state.draft;
    }
};

export default{
    state,
    mutations,
    actions,
    getters
}