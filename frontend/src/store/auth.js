import {create} from 'zustand'
import {mountStoreDevtool} from 'simple-zustand-devtools'

const useAuthStore = create((Set, get)=> ({
    allUserData: null, 
    loading: false,

    user: () => ({
        user: get().allUserData?.user_id || null,
        username: get().allUserData?.username || null,
    }),

    setUser: (user) => set({
        allUserData: user
    }),

    setLoading: (loading) => set({loading}),

    isLogginedIn: () => get().allUserData !== null,
}));

if (import.meta.env.DEV){
    mountStoreDevtool("Store", useAuthStore)
}

export {useAuthStore}