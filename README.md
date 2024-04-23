# Rapid Trip Import

         ()                   * )
                  <^^>             *     (   .
                 .-""-.                    )
      .---.    ."-....-"-._     _...---''`/. '
     ( (`\ \ .'            ``-''    _.-"'`
      \ \ \ : :.                 .-'
       `\`.\: `:.             _.'
       (  .'`.`            _.'
        ``    `-..______.-'
                  ):.  (
                ."-....-".
              .':.        `.
              "-..______..-"

This Idea is very new and in the early days.

Basically this is Rapid Trip Entry for manually entered trips using the existing Trip Import System.

I am still undecided what the final version of this will look like, I am currently thinking browser extension.

Again though if your stumbling across this or something this is still in the 'Hello World' phase.

Also while I build as you can see I will only be using 8 fields (including trip ID), once I am done I am happy with
the foundation of the program I will move to 'Route Genie Template'.

#### Complete

- Basic trip entry in to CSV is complete
    - Trips can be created in single or bulk and then added to csv.
    - trip model checks to make sure ID does not already exist by logging all trips in a different
      file and checking against the file every time a new trip is created.

#### Next

- Perfect trip entry
- Make entries more workable and ensure proper data types are being used

#### Next Next

- Use selenium to automate entry in to RouteGenies existing Trip Import
- Test
- Develop final GUI form


