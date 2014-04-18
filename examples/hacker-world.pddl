;;;; Hacker World - A realistic example
(define (domain hacker-world)

(:requirements :typing
               :negative-preconditions)

(:types hacker non-hacker - person
        pizza burger fries - food
        pepperoni supreme - pizza
        box fridge - container
        person container food software - object)

(:predicates (has-access ?p - person ?s - software)
             (hungry ?p - person)
             (in ?o1 - object ?o2 - object))

;; Eat delicious pizza from a specified place
(:action eat-pizza
  :parameters (?piz - pizza ?per - person ?pla - place)
  :precondition (and (hungry ?per)
                     (in ?pla ?piz))
  :effect (and (not (hungry ?per))
               (not (in ?pla ?piz))
               (in ?per ?piz)))

;; Get access to software of a victim
(:action hack        
  :parameters (?hac - hacker ?sof - software ?per - person)
  :precondition (and (has-access ?per ?sof)
                     (not (hungry ?hac)))
  :effect (and (has-access ?hac ?sof)
               (not (has-access ?per ?sof)))))
