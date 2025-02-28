"use client"
 
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"


const formSchema = z.object({
  username: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
})
 
import React from 'react'
type EventFormProps = {
  userId:string
  type:"Create" | "Update"
}
const EventForm = ({userId, type} : EventFormProps) => {
  return (
    <div>Donate Form{type}</div>
  )
}

export default EventForm